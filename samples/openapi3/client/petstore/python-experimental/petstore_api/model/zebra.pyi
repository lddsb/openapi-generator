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


class Zebra(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "className",
        }
        class properties:
            
            
            class className(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        "zebra": "ZEBRA",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def ZEBRA(cls):
                    return cls("zebra")
            
            
            class type(
                schemas.SchemaEnumMakerClsFactory(
                    enum_value_to_name={
                        "plains": "PLAINS",
                        "mountain": "MOUNTAIN",
                        "grevys": "GREVYS",
                    }
                ),
                schemas.StrSchema
            ):
                
                @classmethod
                @property
                def PLAINS(cls):
                    return cls("plains")
                
                @classmethod
                @property
                def MOUNTAIN(cls):
                    return cls("mountain")
                
                @classmethod
                @property
                def GREVYS(cls):
                    return cls("grevys")
            __annotations__ = {
                "className": className,
                "type": type,
            }
        additional_properties = schemas.AnyTypeSchema
    
    className: MetaOapg.properties.className
    type: typing.Union[MetaOapg.properties.type, schemas.Unset]
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["className"]) -> MetaOapg.properties.className: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def __getitem__(self, name: typing.Union[str, typing.Literal["className"], typing.Literal["type"], ]):
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
        className: typing.Union[MetaOapg.properties.className, str, ],
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'Zebra':
        return super().__new__(
            cls,
            *args,
            className=className,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
