# coding: utf-8

"""
    aptos-api

    The aptos-api provider  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

from openapi_aptos_api import schemas  # noqa: F401


class GetCoinTransfersByBlockHeightsResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "cursor",
            "result",
            "hasNextPage",
        }
        
        class properties:
            
            
            class cursor(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'cursor':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            hasNextPage = schemas.BoolSchema
            
            
            class result(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    max_items = 100
                    min_items = 0
                    
                    @staticmethod
                    def items() -> typing.Type['CoinTransferDto']:
                        return CoinTransferDto
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CoinTransferDto'], typing.List['CoinTransferDto']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'result':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CoinTransferDto':
                    return super().__getitem__(i)
            __annotations__ = {
                "cursor": cursor,
                "hasNextPage": hasNextPage,
                "result": result,
            }
    
    cursor: MetaOapg.properties.cursor
    result: MetaOapg.properties.result
    hasNextPage: MetaOapg.properties.hasNextPage
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cursor"]) -> MetaOapg.properties.cursor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasNextPage"]) -> MetaOapg.properties.hasNextPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cursor", "hasNextPage", "result", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cursor"]) -> MetaOapg.properties.cursor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hasNextPage"]) -> MetaOapg.properties.hasNextPage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cursor", "hasNextPage", "result", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cursor: typing.Union[MetaOapg.properties.cursor, None, str, ],
        result: typing.Union[MetaOapg.properties.result, list, tuple, ],
        hasNextPage: typing.Union[MetaOapg.properties.hasNextPage, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetCoinTransfersByBlockHeightsResponse':
        return super().__new__(
            cls,
            *args,
            cursor=cursor,
            result=result,
            hasNextPage=hasNextPage,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_aptos_api.model.coin_transfer_dto import CoinTransferDto
