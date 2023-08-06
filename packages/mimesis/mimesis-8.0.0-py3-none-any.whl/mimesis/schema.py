"""Implements classes for generating data by schema."""

import csv
import json
import pickle
import re
import typing as t
import warnings

from mimesis.exceptions import FieldError, FieldsetError, SchemaError
from mimesis.locales import Locale
from mimesis.providers.base import BaseProvider
from mimesis.providers.generic import Generic
from mimesis.types import (
    JSON,
    CallableSchema,
    FieldCache,
    Key,
    MissingSeed,
    Seed,
)

__all__ = ["BaseField", "Field", "Fieldset", "Schema"]


class BaseField:
    def __init__(
        self,
        locale: Locale = Locale.DEFAULT,
        seed: Seed = MissingSeed,
        providers: t.Optional[t.Sequence[t.Any]] = None,
    ) -> None:
        """Initialize field.

        :param locale: Locale
        :param seed: Seed for random.
        """
        self._gen = Generic(locale, seed)

        if providers:
            self._gen.add_providers(*providers)

        self._cache: FieldCache = {}

    def reseed(self, seed: Seed = MissingSeed) -> None:
        """Reseed the random generator.

        :param seed: Seed for random.
        """
        self._gen.reseed(seed)

    def _explicit_lookup(self, name: str) -> t.Any:
        """An explicit method lookup.

        This method is called when the field
        defined explicitly, like this: ``provider.method``

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        provider_name, method_name = name.split(".", 1)
        try:
            provider = getattr(self._gen, provider_name)
            return getattr(provider, method_name)
        except AttributeError:
            raise FieldError(name)

    def _fuzzy_lookup(self, name: str) -> t.Any:
        """A fuzzy method lookup.

        This method is called when the field definition
        is fuzzy, like this: ``method``

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        for provider in dir(self._gen):
            provider = getattr(self._gen, provider)
            if isinstance(provider, BaseProvider):
                if name in dir(provider):
                    return getattr(provider, name)

        raise FieldError(name)

    def _lookup_method(self, name: str) -> t.Any:
        """Lookup method by the field name.

        :param name: The field name.
        :return: Callable object.
        :raise FieldError: When field is invalid.
        """
        # Support additional delimiters
        name = re.sub(r"[/:\s]", ".", name)

        if name.count(".") > 1:
            raise FieldError(name)

        if name not in self._cache:
            if "." not in name:
                method = self._fuzzy_lookup(name)
            else:
                method = self._explicit_lookup(name)
            self._cache[name] = method

        return self._cache[name]

    def perform(
        self,
        name: t.Optional[str] = None,
        key: Key = None,
        **kwargs: t.Any,
    ) -> t.Any:
        """Performs the value of the field by its name.

        It takes any string which represents the name of any method of
        any supported data provider and the ``**kwargs`` of this method.

        .. note:: Some data providers have methods with the same names
            and in such cases, you can explicitly define that the method
            belongs to data-provider ``name='provider.name'`` otherwise
            it will return the data from the first provider which
            has a method ``name``.

            Allowed delimiters: ``.``, ``:``, ``/`` and space:

            - ``provider.name``
            - ``provider:name``
            - ``provider/name``
            - ``provider name``

        You can apply a *key function* to the result returned by
        the method, by passing a parameter **key** with a callable
        object which returns the final result.

        :param name: Name of the method.
        :param key: A key function (or any other callable object)
            which will be applied to result.
        :param kwargs: Kwargs of method.
        :return: Value which represented by method.
        :raises ValueError: if provider not
            supported or if field not defined.
        """
        if name is None:
            raise FieldError()

        result = self._lookup_method(name)(**kwargs)

        if key and callable(key):
            return key(result)

        return result

    def __str__(self) -> str:
        return f"{self.__class__.__name__} <{self._gen.locale}>"


class Field(BaseField):
    """Greedy field.

    The field whcih evaluates immediately.

    .. warning::

        There is no case when you need to instance **field** in loops.

        If you doing this:

        .. code-block:: python

            for i in range(1000):
                field = Field()

        You doing it **wrong**! It is a terrible idea that will lead to a memory leak.

        Forewarned is forearmed.

    Here is usage example:

        >>> _ = Field()
        >>> _('username')
        Dogtag_1836
    """

    def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        return self.perform(*args, **kwargs)


class Fieldset(BaseField):
    """Greedy fieldset (evaluates immediately).

    Works like a field, but returns a list of values.

    Here is usage example:

        >>> fieldset = Fieldset(i=100)
        >>> fieldset('username')
        ['pot_1821', 'vhs_1915', ..., 'reviewed_1849']

    You may also specify the number of iterations by passing the **i** keyword
    argument to the callable instance of fieldset:

        >>> fieldset = Fieldset()
        >>> fieldset('username', i=2)
        ['pot_1821', 'vhs_1915']

    When **i** is not specified, the reasonable default is used — **10**.

    See "Field vs Fieldset" section of documentation for more details.

    :cvar fieldset_default_iterations: Default iterations. Default is **10**.
    :cvar fieldset_iterations_kwarg: Keyword argument for iterations. Default is **i**.
    """

    fieldset_default_iterations: int = 10
    fieldset_iterations_kwarg: str = "i"

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize fieldset.

        Accepts additional keyword argument **i** which is used
        to specify the number of iterations.

        The name of the keyword argument can be changed by
        overriding **fieldset_iterations_kwarg** attribute of this class.
        """
        self._iterations = kwargs.pop(
            self.fieldset_iterations_kwarg,
            self.fieldset_default_iterations,
        )
        super().__init__(*args, **kwargs)

    def __call__(self, *args: t.Any, **kwargs: t.Any) -> t.List[t.Any]:
        """Perform fieldset.

        :param args: Arguments for field.
        :param kwargs: Keyword arguments for field.
        :raises FieldsetError: If iterations less than 1.
        :return: List of values.
        """
        min_iterations = 1
        iterations = kwargs.pop(
            self.fieldset_iterations_kwarg,
            self._iterations,
        )

        if iterations < min_iterations:
            raise FieldsetError()

        return [self.perform(*args, **kwargs) for _ in range(iterations)]


class Schema:
    """Class which return list of filled schemas."""

    _MIN_ITERATIONS_VALUE: t.ClassVar[int] = 1

    __slots__ = ("_schema",)

    def __init__(self, schema: CallableSchema) -> None:
        """Initialize schema.

        :param schema: A schema (must be a callable object).
        """
        if schema and callable(schema):  # type: ignore[truthy-function]
            self._schema = schema
        else:
            # This is just a better error message
            raise SchemaError()

    def __mul__(self, other: int) -> t.List[JSON]:
        """Multiplies the schema by the number of iterations.

        Schema multiplication is not lazy, so it will be performed immediately (in fact,
        you're using :meth:`~mimesis.schema.Schema.create` under the hood).

        .. warning::

            Multiplying the large and nested schema with a large number is obviously
            a `stupid`_ idea, so **be reasonable** on choosing a multiplier.

            .. _stupid: https://dictionary.cambridge.org/dictionary/english/stupid

        Usage:

        .. code-block:: python

            schema = Schema(lambda: {
                'email': _('username'),
                'token': _('token_hex', key=lambda x: x[:8])
            })
            print(schema * 2)
            print(2 * schema)

        .. note::

            Keep in mind the priority and order of multipliers.

            Instead of doing this:

            >>> schema * 2 * 10

            Where you evaluate the schema 2 times and then multiply the resulting list 10 times, you should do this:

            >>> schema * (2 * 10) # Evaluates the schema 20 times.

            In other words, the first multiplier evaluetes the schema:

            >>> 1 * schema * 3

            The result will be:

            .. code-block:: json

                [
                    {"email": "efforts1859@test.com", "token": "f4a29754"},
                    {"email": "efforts1859@test.com", "token": "f4a29754"},
                    {"email": "efforts1859@test.com", "token": "f4a29754"},
                ]

            Because schema is evaluated first (`1 * schema`), and then the second multiplier is
            applied on the result of the first expression since.

        :param other: The multiplier.
        """
        return self.create(other)

    def __rmul__(self, other: int) -> t.List[JSON]:
        return self.__mul__(other)

    def to_csv(self, file_path: str, iterations: int = 100, **kwargs: t.Any) -> None:
        """Export a schema as a CSV file.

        :param file_path: File path.
        :param iterations: The required number of rows.
        :param kwargs: The keyword arguments for :py:class:`csv.DictWriter` class.

        *New in version 5.3.0*
        """
        data = self.create(iterations)
        fieldnames = list(data[0])

        with open(file_path, "w", encoding="utf-8", newline="") as fp:
            dict_writer = csv.DictWriter(fp, fieldnames, **kwargs)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    def to_json(self, file_path: str, iterations: int = 100, **kwargs: t.Any) -> None:
        """Export a schema as a JSON file.

        :param file_path: File path.
        :param iterations: The required number of rows.
        :param kwargs: Extra keyword arguments for :py:func:`json.dump` class.

        *New in version 5.3.0*
        """
        data = self.create(iterations)
        with open(file_path, "w", encoding="utf-8") as fp:
            json.dump(data, fp, **kwargs)

    def to_pickle(self, file_path: str, iterations: int = 100, **kwargs: t.Any) -> None:
        """Export a schema as the pickled representation of the object to the file.

        :param file_path: File path.
        :param iterations: The required number of rows.
        :param kwargs: Extra keyword arguments for :py:func:`pickle.dump` class.

        *New in version 5.3.0*
        """
        data = self.create(iterations)
        with open(file_path, "wb") as fp:
            pickle.dump(data, fp, **kwargs)

    def create(self, iterations: int = 1) -> t.List[JSON]:
        """Creates a list of a fulfilled schemas.

        .. note::
            This method evaluates immediately, so be careful on creating
            large datasets otherwise you're risking running out of memory.

            If you need a lazy version of this method, see :meth:`iterator`.

        :param iterations: Number of iterations.
        :return: List of fulfilled schemas.
        """

        if iterations < self._MIN_ITERATIONS_VALUE:
            raise ValueError("The number of iterations must be greater than 0.")

        return [self._schema() for _ in range(iterations)]

    def loop(self) -> t.Iterator[JSON]:
        """Fulfills a schema **infinitely** in a lazy way.

        This method can be useful when you have dynamic conditions
        on which the generation must depend and be interrupted accordingly.

        Since the data provided by mimesis is limited, frequent
        calls of this method may cause data duplication.

        Before using this method, ask yourself: **Do I really need this**?
        In most cases, the answer is: Nah, :meth:`iterator` is enough.

        **Do not use** this method without **interrupt conditions**, otherwise,
        you're risking running out of memory.

        If you're accepting all risks below and want to suppress
        the warnings then use :py:class:`warnings.catch_warnings`

        .. warning::

            **Never** (seriously) call :py:class:`list`, :py:class:`tuple`, :py:class:`set`
            or any other callable which tries to evaluate the whole lazy object on this
            method — **infinite** called infinite for a reason.

        :return: An infinite iterator with fulfilled schemas.
        """

        warnings.warn(
            "You're iterating over the infinite object! "
            "The schema.loop() may cause a serious memory leak."
            "Please, see: https://mimesis.name/en/latest/api.html#mimesis.schema.Schema.loop"
        )

        while True:
            yield self._schema()

    def iterator(self, iterations: int = 1) -> t.Iterator[JSON]:
        """Fulfills schema in a lazy way.

        :param iterations: Number of iterations.
        :return: List of fulfilled schemas.
        """

        if iterations < self._MIN_ITERATIONS_VALUE:
            raise ValueError("The number of iterations must be greater than 0.")

        for item in range(iterations):
            yield self._schema()
