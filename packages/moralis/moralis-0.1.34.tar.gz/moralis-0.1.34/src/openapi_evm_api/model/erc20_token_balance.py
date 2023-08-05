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


class Erc20TokenBalance(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "symbol",
            "balance",
            "possible_spam",
            "decimals",
            "name",
            "token_address",
        }
        
        class properties:
            token_address = schemas.StrSchema
            name = schemas.StrSchema
            symbol = schemas.StrSchema
            decimals = schemas.IntSchema
            balance = schemas.StrSchema
            possible_spam = schemas.BoolSchema
            logo = schemas.StrSchema
            thumbnail = schemas.StrSchema
            __annotations__ = {
                "token_address": token_address,
                "name": name,
                "symbol": symbol,
                "decimals": decimals,
                "balance": balance,
                "possible_spam": possible_spam,
                "logo": logo,
                "thumbnail": thumbnail,
            }

    
    symbol: MetaOapg.properties.symbol
    balance: MetaOapg.properties.balance
    possible_spam: MetaOapg.properties.possible_spam
    decimals: MetaOapg.properties.decimals
    name: MetaOapg.properties.name
    token_address: MetaOapg.properties.token_address
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["thumbnail"]) -> MetaOapg.properties.thumbnail: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["token_address", "name", "symbol", "decimals", "balance", "possible_spam", "logo", "thumbnail", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["token_address"]) -> MetaOapg.properties.token_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["possible_spam"]) -> MetaOapg.properties.possible_spam: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["thumbnail"]) -> typing.Union[MetaOapg.properties.thumbnail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["token_address", "name", "symbol", "decimals", "balance", "possible_spam", "logo", "thumbnail", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        symbol: typing.Union[MetaOapg.properties.symbol, str, ],
        balance: typing.Union[MetaOapg.properties.balance, str, ],
        possible_spam: typing.Union[MetaOapg.properties.possible_spam, bool, ],
        decimals: typing.Union[MetaOapg.properties.decimals, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        token_address: typing.Union[MetaOapg.properties.token_address, str, ],
        logo: typing.Union[MetaOapg.properties.logo, str, schemas.Unset] = schemas.unset,
        thumbnail: typing.Union[MetaOapg.properties.thumbnail, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Erc20TokenBalance':
        return super().__new__(
            cls,
            *args,
            symbol=symbol,
            balance=balance,
            possible_spam=possible_spam,
            decimals=decimals,
            name=name,
            token_address=token_address,
            logo=logo,
            thumbnail=thumbnail,
            _configuration=_configuration,
            **kwargs,
        )
