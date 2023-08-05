# coding: utf-8

"""
    EVM API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 2.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_evm_api import schemas  # noqa: F401


class NormalizedMetadataAttribute(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            trait_type = schemas.StrSchema
            value = schemas.DictSchema
            display_type = schemas.StrSchema
            max_value = schemas.NumberSchema
            trait_count = schemas.NumberSchema
            order = schemas.NumberSchema
            __annotations__ = {
                "trait_type": trait_type,
                "value": value,
                "display_type": display_type,
                "max_value": max_value,
                "trait_count": trait_count,
                "order": order,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trait_type"]) -> MetaOapg.properties.trait_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_type"]) -> MetaOapg.properties.display_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_value"]) -> MetaOapg.properties.max_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trait_count"]) -> MetaOapg.properties.trait_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["trait_type", "value", "display_type", "max_value", "trait_count", "order", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trait_type"]) -> typing.Union[MetaOapg.properties.trait_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_type"]) -> typing.Union[MetaOapg.properties.display_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_value"]) -> typing.Union[MetaOapg.properties.max_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trait_count"]) -> typing.Union[MetaOapg.properties.trait_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["trait_type", "value", "display_type", "max_value", "trait_count", "order", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        trait_type: typing.Union[MetaOapg.properties.trait_type, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        display_type: typing.Union[MetaOapg.properties.display_type, str, schemas.Unset] = schemas.unset,
        max_value: typing.Union[MetaOapg.properties.max_value, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        trait_count: typing.Union[MetaOapg.properties.trait_count, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NormalizedMetadataAttribute':
        return super().__new__(
            cls,
            *args,
            trait_type=trait_type,
            value=value,
            display_type=display_type,
            max_value=max_value,
            trait_count=trait_count,
            order=order,
            _configuration=_configuration,
            **kwargs,
        )
