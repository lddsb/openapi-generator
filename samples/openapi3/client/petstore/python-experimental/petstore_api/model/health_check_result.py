# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

from petstore_api import schemas  # noqa: F401


class HealthCheckResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Just a string to inform instance is up and running. Make it nullable in hope to get it as pointer in generated model.
    """


    class MetaOapg:
        class properties:
            
            
            class NullableMessage(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, str, ]),
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'NullableMessage':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "NullableMessage": NullableMessage,
            }
        additional_properties = schemas.AnyTypeSchema
    
    NullableMessage: typing.Union[MetaOapg.properties.NullableMessage, schemas.Unset]
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["NullableMessage"]) -> typing.Union[MetaOapg.properties.NullableMessage, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def __getitem__(self, name: typing.Union[str, typing.Literal["NullableMessage"], ]):
        # dict_instance[name] accessor
        if not hasattr(self.MetaOapg, 'properties') or name not in self.MetaOapg.properties.__annotations__:
            return super().__getitem__(name)
        try:
            return super().__getitem__(name)
        except KeyError:
            return schemas.unset

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        NullableMessage: typing.Union[MetaOapg.properties.NullableMessage, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'HealthCheckResult':
        return super().__new__(
            cls,
            *args,
            NullableMessage=NullableMessage,
            _configuration=_configuration,
            **kwargs,
        )
