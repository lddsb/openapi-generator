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


class User(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        class properties:
            id = schemas.Int64Schema
            username = schemas.StrSchema
            firstName = schemas.StrSchema
            lastName = schemas.StrSchema
            email = schemas.StrSchema
            password = schemas.StrSchema
            phone = schemas.StrSchema
            userStatus = schemas.Int32Schema
            objectWithNoDeclaredProps = schemas.DictSchema
            
            
            class objectWithNoDeclaredPropsNullable(
                schemas.SchemaTypeCheckerClsFactory(typing.Union[schemas.NoneClass, frozendict.frozendict, ]),
                schemas.DictBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneFrozenDictMixin
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
            
                
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
                    *args: typing.Union[dict, frozendict.frozendict, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
                ) -> 'objectWithNoDeclaredPropsNullable':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            anyTypeProp = schemas.AnyTypeSchema
            
            
            class anyTypeExceptNullProp(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    additional_properties = schemas.AnyTypeSchema
                    not_schema = schemas.NoneSchema
            
                
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
                ) -> 'anyTypeExceptNullProp':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            anyTypePropNullable = schemas.AnyTypeSchema
            __annotations__ = {
                "id": id,
                "username": username,
                "firstName": firstName,
                "lastName": lastName,
                "email": email,
                "password": password,
                "phone": phone,
                "userStatus": userStatus,
                "objectWithNoDeclaredProps": objectWithNoDeclaredProps,
                "objectWithNoDeclaredPropsNullable": objectWithNoDeclaredPropsNullable,
                "anyTypeProp": anyTypeProp,
                "anyTypeExceptNullProp": anyTypeExceptNullProp,
                "anyTypePropNullable": anyTypePropNullable,
            }
        additional_properties = schemas.AnyTypeSchema
    
    id: typing.Union[MetaOapg.properties.id, schemas.Unset]
    username: typing.Union[MetaOapg.properties.username, schemas.Unset]
    firstName: typing.Union[MetaOapg.properties.firstName, schemas.Unset]
    lastName: typing.Union[MetaOapg.properties.lastName, schemas.Unset]
    email: typing.Union[MetaOapg.properties.email, schemas.Unset]
    password: typing.Union[MetaOapg.properties.password, schemas.Unset]
    phone: typing.Union[MetaOapg.properties.phone, schemas.Unset]
    userStatus: typing.Union[MetaOapg.properties.userStatus, schemas.Unset]
    objectWithNoDeclaredProps: typing.Union[MetaOapg.properties.objectWithNoDeclaredProps, schemas.Unset]
    objectWithNoDeclaredPropsNullable: typing.Union[MetaOapg.properties.objectWithNoDeclaredPropsNullable, schemas.Unset]
    anyTypeProp: typing.Union[MetaOapg.properties.anyTypeProp, schemas.Unset]
    anyTypeExceptNullProp: typing.Union[MetaOapg.properties.anyTypeExceptNullProp, schemas.Unset]
    anyTypePropNullable: typing.Union[MetaOapg.properties.anyTypePropNullable, schemas.Unset]
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["userStatus"]) -> typing.Union[MetaOapg.properties.userStatus, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["objectWithNoDeclaredProps"]) -> typing.Union[MetaOapg.properties.objectWithNoDeclaredProps, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["objectWithNoDeclaredPropsNullable"]) -> typing.Union[MetaOapg.properties.objectWithNoDeclaredPropsNullable, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["anyTypeProp"]) -> typing.Union[MetaOapg.properties.anyTypeProp, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["anyTypeExceptNullProp"]) -> typing.Union[MetaOapg.properties.anyTypeExceptNullProp, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: typing.Literal["anyTypePropNullable"]) -> typing.Union[MetaOapg.properties.anyTypePropNullable, schemas.Unset]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> typing.Union[MetaOapg.additional_properties, schemas.Unset]: ...
    
    def __getitem__(self, name: typing.Union[str, typing.Literal["id"], typing.Literal["username"], typing.Literal["firstName"], typing.Literal["lastName"], typing.Literal["email"], typing.Literal["password"], typing.Literal["phone"], typing.Literal["userStatus"], typing.Literal["objectWithNoDeclaredProps"], typing.Literal["objectWithNoDeclaredPropsNullable"], typing.Literal["anyTypeProp"], typing.Literal["anyTypeExceptNullProp"], typing.Literal["anyTypePropNullable"], ]):
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
        id: typing.Union[MetaOapg.properties.id, int, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        userStatus: typing.Union[MetaOapg.properties.userStatus, int, schemas.Unset] = schemas.unset,
        objectWithNoDeclaredProps: typing.Union[MetaOapg.properties.objectWithNoDeclaredProps, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        objectWithNoDeclaredPropsNullable: typing.Union[MetaOapg.properties.objectWithNoDeclaredPropsNullable, dict, frozendict.frozendict, None, schemas.Unset] = schemas.unset,
        anyTypeProp: typing.Union[MetaOapg.properties.anyTypeProp, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, schemas.Unset] = schemas.unset,
        anyTypeExceptNullProp: typing.Union[MetaOapg.properties.anyTypeExceptNullProp, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, schemas.Unset] = schemas.unset,
        anyTypePropNullable: typing.Union[MetaOapg.properties.anyTypePropNullable, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.additional_properties, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes, ],
    ) -> 'User':
        return super().__new__(
            cls,
            *args,
            id=id,
            username=username,
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password,
            phone=phone,
            userStatus=userStatus,
            objectWithNoDeclaredProps=objectWithNoDeclaredProps,
            objectWithNoDeclaredPropsNullable=objectWithNoDeclaredPropsNullable,
            anyTypeProp=anyTypeProp,
            anyTypeExceptNullProp=anyTypeExceptNullProp,
            anyTypePropNullable=anyTypePropNullable,
            _configuration=_configuration,
            **kwargs,
        )
