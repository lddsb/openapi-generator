# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class ForbiddenProperty(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
            
            
            class foo(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                    not_schema = schemas.AnyTypeSchema
            
                
                def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                    # dict_instance[name] accessor
                    if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
                        return super().__getitem__(name)
                    try:
                        return super().__getitem__(name)
                    except KeyError:
                        return schemas.unset
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
                ) -> 'foo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "foo": foo,
            }
        additional_properties = schemas.AnyTypeSchema

    
    foo: typing.Union[MetaOapg.properties.foo, schemas.Unset]
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["foo"]) -> typing.Union[MetaOapg.properties.foo, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def __getitem__(self, name: typing.Union[str, typing.Literal["foo"], ]):
        # dict_instance[name] accessor
        if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
            return super().__getitem__(name)
        try:
            return super().__getitem__(name)
        except KeyError:
            return schemas.unset

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
        foo: typing.Union[MetaOapg.properties.foo, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'ForbiddenProperty':
        return super().__new__(
            cls,
            *args,
            foo=foo,
            _configuration=_configuration,
            **kwargs,
        )
