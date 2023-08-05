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


class NftContractMetadataCollection(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "result",
            "total",
            "page",
            "page_size",
        }
        
        class properties:
            total = schemas.IntSchema
            page = schemas.IntSchema
            page_size = schemas.IntSchema
            
            
            class result(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NftContractMetadata']:
                        return NftContractMetadata
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['NftContractMetadata'], typing.List['NftContractMetadata']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'result':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NftContractMetadata':
                    return super().__getitem__(i)
            __annotations__ = {
                "total": total,
                "page": page,
                "page_size": page_size,
                "result": result,
            }

    
    result: MetaOapg.properties.result
    total: MetaOapg.properties.total
    page: MetaOapg.properties.page
    page_size: MetaOapg.properties.page_size
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["page_size"]) -> MetaOapg.properties.page_size: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["total", "page", "page_size", "result", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total"]) -> MetaOapg.properties.total: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page"]) -> MetaOapg.properties.page: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["page_size"]) -> MetaOapg.properties.page_size: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["total", "page", "page_size", "result", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        result: typing.Union[MetaOapg.properties.result, list, tuple, ],
        total: typing.Union[MetaOapg.properties.total, decimal.Decimal, int, ],
        page: typing.Union[MetaOapg.properties.page, decimal.Decimal, int, ],
        page_size: typing.Union[MetaOapg.properties.page_size, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NftContractMetadataCollection':
        return super().__new__(
            cls,
            *args,
            result=result,
            total=total,
            page=page,
            page_size=page_size,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_evm_api.model.nft_contract_metadata import NftContractMetadata
