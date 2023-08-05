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


class CoinTransferDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "amount",
            "coin_type",
            "is_transaction_success",
            "event_sequence_number",
            "owner_address",
            "transaction_timestamp",
            "block_height",
            "event_creation_number",
            "event_account_address",
            "activity_type",
            "entry_function_id_str",
            "transaction_version",
            "is_gas_fee",
        }
        
        class properties:
            
            
            class activity_type(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 200
                    min_length = 1
            
            
            class amount(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 200
                    min_length = 1
            
            
            class block_height(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 200
                    min_length = 1
            
            
            class coin_type(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 5000
                    min_length = 1
            
            
            class entry_function_id_str(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 100
                    min_length = 1
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'entry_function_id_str':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class event_account_address(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 66
                    min_length = 66
            
            
            class event_creation_number(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 66
                    min_length = 1
            
            
            class event_sequence_number(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 66
                    min_length = 1
            is_gas_fee = schemas.BoolSchema
            is_transaction_success = schemas.BoolSchema
            
            
            class owner_address(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 66
                    min_length = 66
            transaction_timestamp = schemas.StrSchema
            transaction_version = schemas.StrSchema
            __annotations__ = {
                "activity_type": activity_type,
                "amount": amount,
                "block_height": block_height,
                "coin_type": coin_type,
                "entry_function_id_str": entry_function_id_str,
                "event_account_address": event_account_address,
                "event_creation_number": event_creation_number,
                "event_sequence_number": event_sequence_number,
                "is_gas_fee": is_gas_fee,
                "is_transaction_success": is_transaction_success,
                "owner_address": owner_address,
                "transaction_timestamp": transaction_timestamp,
                "transaction_version": transaction_version,
            }
    
    amount: MetaOapg.properties.amount
    coin_type: MetaOapg.properties.coin_type
    is_transaction_success: MetaOapg.properties.is_transaction_success
    event_sequence_number: MetaOapg.properties.event_sequence_number
    owner_address: MetaOapg.properties.owner_address
    transaction_timestamp: MetaOapg.properties.transaction_timestamp
    block_height: MetaOapg.properties.block_height
    event_creation_number: MetaOapg.properties.event_creation_number
    event_account_address: MetaOapg.properties.event_account_address
    activity_type: MetaOapg.properties.activity_type
    entry_function_id_str: MetaOapg.properties.entry_function_id_str
    transaction_version: MetaOapg.properties.transaction_version
    is_gas_fee: MetaOapg.properties.is_gas_fee
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activity_type"]) -> MetaOapg.properties.activity_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["block_height"]) -> MetaOapg.properties.block_height: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["coin_type"]) -> MetaOapg.properties.coin_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entry_function_id_str"]) -> MetaOapg.properties.entry_function_id_str: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_account_address"]) -> MetaOapg.properties.event_account_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_creation_number"]) -> MetaOapg.properties.event_creation_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_sequence_number"]) -> MetaOapg.properties.event_sequence_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_gas_fee"]) -> MetaOapg.properties.is_gas_fee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_transaction_success"]) -> MetaOapg.properties.is_transaction_success: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_address"]) -> MetaOapg.properties.owner_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_timestamp"]) -> MetaOapg.properties.transaction_timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_version"]) -> MetaOapg.properties.transaction_version: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["activity_type", "amount", "block_height", "coin_type", "entry_function_id_str", "event_account_address", "event_creation_number", "event_sequence_number", "is_gas_fee", "is_transaction_success", "owner_address", "transaction_timestamp", "transaction_version", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activity_type"]) -> MetaOapg.properties.activity_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["block_height"]) -> MetaOapg.properties.block_height: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["coin_type"]) -> MetaOapg.properties.coin_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entry_function_id_str"]) -> MetaOapg.properties.entry_function_id_str: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_account_address"]) -> MetaOapg.properties.event_account_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_creation_number"]) -> MetaOapg.properties.event_creation_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_sequence_number"]) -> MetaOapg.properties.event_sequence_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_gas_fee"]) -> MetaOapg.properties.is_gas_fee: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_transaction_success"]) -> MetaOapg.properties.is_transaction_success: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_address"]) -> MetaOapg.properties.owner_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_timestamp"]) -> MetaOapg.properties.transaction_timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_version"]) -> MetaOapg.properties.transaction_version: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["activity_type", "amount", "block_height", "coin_type", "entry_function_id_str", "event_account_address", "event_creation_number", "event_sequence_number", "is_gas_fee", "is_transaction_success", "owner_address", "transaction_timestamp", "transaction_version", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, ],
        coin_type: typing.Union[MetaOapg.properties.coin_type, str, ],
        is_transaction_success: typing.Union[MetaOapg.properties.is_transaction_success, bool, ],
        event_sequence_number: typing.Union[MetaOapg.properties.event_sequence_number, str, ],
        owner_address: typing.Union[MetaOapg.properties.owner_address, str, ],
        transaction_timestamp: typing.Union[MetaOapg.properties.transaction_timestamp, str, ],
        block_height: typing.Union[MetaOapg.properties.block_height, str, ],
        event_creation_number: typing.Union[MetaOapg.properties.event_creation_number, str, ],
        event_account_address: typing.Union[MetaOapg.properties.event_account_address, str, ],
        activity_type: typing.Union[MetaOapg.properties.activity_type, str, ],
        entry_function_id_str: typing.Union[MetaOapg.properties.entry_function_id_str, None, str, ],
        transaction_version: typing.Union[MetaOapg.properties.transaction_version, str, ],
        is_gas_fee: typing.Union[MetaOapg.properties.is_gas_fee, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CoinTransferDto':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            coin_type=coin_type,
            is_transaction_success=is_transaction_success,
            event_sequence_number=event_sequence_number,
            owner_address=owner_address,
            transaction_timestamp=transaction_timestamp,
            block_height=block_height,
            event_creation_number=event_creation_number,
            event_account_address=event_account_address,
            activity_type=activity_type,
            entry_function_id_str=entry_function_id_str,
            transaction_version=transaction_version,
            is_gas_fee=is_gas_fee,
            _configuration=_configuration,
            **kwargs,
        )
