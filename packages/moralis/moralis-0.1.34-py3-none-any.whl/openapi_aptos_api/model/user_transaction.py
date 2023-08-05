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


class UserTransaction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "signature",
            "event_root_hash",
            "gas_used",
            "changes",
            "state_checkpoint_hash",
            "state_change_hash",
            "accumulator_root_hash",
            "type",
            "version",
            "expiration_timestamp_secs",
            "sequence_number",
            "vm_status",
            "payload",
            "sender",
            "success",
            "gas_unit_price",
            "max_gas_amount",
            "events",
            "hash",
            "timestamp",
        }
        
        class properties:
            type = schemas.StrSchema
            version = schemas.StrSchema
            hash = schemas.StrSchema
            state_change_hash = schemas.StrSchema
            event_root_hash = schemas.StrSchema
            state_checkpoint_hash = schemas.StrSchema
            gas_used = schemas.StrSchema
            success = schemas.BoolSchema
            vm_status = schemas.StrSchema
            accumulator_root_hash = schemas.StrSchema
            
            
            class changes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            @classmethod
                            @functools.lru_cache()
                            def any_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    DeleteModuleChange,
                                    DeleteResourceChange,
                                    DeleteTableItemChange,
                                    WriteOrUpdateModuleChange,
                                    WriteResourceChange,
                                    WriteTableChangeSetChange,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'changes':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            sender = schemas.StrSchema
            sequence_number = schemas.StrSchema
            max_gas_amount = schemas.StrSchema
            gas_unit_price = schemas.StrSchema
            expiration_timestamp_secs = schemas.StrSchema
            
            
            class payload(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            EntryFunctionPayloadRequest,
                            ScriptPayloadRequest,
                            ModuleBundlePayloadRequest,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'payload':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class signature(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            Ed25519SignatureRequest,
                            MultiEd25519SignatureRequest,
                            MultiAgentSignatureRequest,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'signature':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class events(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TransactionEvent']:
                        return TransactionEvent
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TransactionEvent'], typing.List['TransactionEvent']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'events':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TransactionEvent':
                    return super().__getitem__(i)
            timestamp = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "version": version,
                "hash": hash,
                "state_change_hash": state_change_hash,
                "event_root_hash": event_root_hash,
                "state_checkpoint_hash": state_checkpoint_hash,
                "gas_used": gas_used,
                "success": success,
                "vm_status": vm_status,
                "accumulator_root_hash": accumulator_root_hash,
                "changes": changes,
                "sender": sender,
                "sequence_number": sequence_number,
                "max_gas_amount": max_gas_amount,
                "gas_unit_price": gas_unit_price,
                "expiration_timestamp_secs": expiration_timestamp_secs,
                "payload": payload,
                "signature": signature,
                "events": events,
                "timestamp": timestamp,
            }
    
    signature: MetaOapg.properties.signature
    event_root_hash: MetaOapg.properties.event_root_hash
    gas_used: MetaOapg.properties.gas_used
    changes: MetaOapg.properties.changes
    state_checkpoint_hash: MetaOapg.properties.state_checkpoint_hash
    state_change_hash: MetaOapg.properties.state_change_hash
    accumulator_root_hash: MetaOapg.properties.accumulator_root_hash
    type: MetaOapg.properties.type
    version: MetaOapg.properties.version
    expiration_timestamp_secs: MetaOapg.properties.expiration_timestamp_secs
    sequence_number: MetaOapg.properties.sequence_number
    vm_status: MetaOapg.properties.vm_status
    payload: MetaOapg.properties.payload
    sender: MetaOapg.properties.sender
    success: MetaOapg.properties.success
    gas_unit_price: MetaOapg.properties.gas_unit_price
    max_gas_amount: MetaOapg.properties.max_gas_amount
    events: MetaOapg.properties.events
    hash: MetaOapg.properties.hash
    timestamp: MetaOapg.properties.timestamp
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state_change_hash"]) -> MetaOapg.properties.state_change_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["event_root_hash"]) -> MetaOapg.properties.event_root_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state_checkpoint_hash"]) -> MetaOapg.properties.state_checkpoint_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas_used"]) -> MetaOapg.properties.gas_used: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vm_status"]) -> MetaOapg.properties.vm_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accumulator_root_hash"]) -> MetaOapg.properties.accumulator_root_hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changes"]) -> MetaOapg.properties.changes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sender"]) -> MetaOapg.properties.sender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequence_number"]) -> MetaOapg.properties.sequence_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max_gas_amount"]) -> MetaOapg.properties.max_gas_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gas_unit_price"]) -> MetaOapg.properties.gas_unit_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration_timestamp_secs"]) -> MetaOapg.properties.expiration_timestamp_secs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature"]) -> MetaOapg.properties.signature: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "version", "hash", "state_change_hash", "event_root_hash", "state_checkpoint_hash", "gas_used", "success", "vm_status", "accumulator_root_hash", "changes", "sender", "sequence_number", "max_gas_amount", "gas_unit_price", "expiration_timestamp_secs", "payload", "signature", "events", "timestamp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state_change_hash"]) -> MetaOapg.properties.state_change_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["event_root_hash"]) -> MetaOapg.properties.event_root_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state_checkpoint_hash"]) -> MetaOapg.properties.state_checkpoint_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas_used"]) -> MetaOapg.properties.gas_used: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["success"]) -> MetaOapg.properties.success: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vm_status"]) -> MetaOapg.properties.vm_status: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accumulator_root_hash"]) -> MetaOapg.properties.accumulator_root_hash: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changes"]) -> MetaOapg.properties.changes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sender"]) -> MetaOapg.properties.sender: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sequence_number"]) -> MetaOapg.properties.sequence_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max_gas_amount"]) -> MetaOapg.properties.max_gas_amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gas_unit_price"]) -> MetaOapg.properties.gas_unit_price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration_timestamp_secs"]) -> MetaOapg.properties.expiration_timestamp_secs: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payload"]) -> MetaOapg.properties.payload: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature"]) -> MetaOapg.properties.signature: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "version", "hash", "state_change_hash", "event_root_hash", "state_checkpoint_hash", "gas_used", "success", "vm_status", "accumulator_root_hash", "changes", "sender", "sequence_number", "max_gas_amount", "gas_unit_price", "expiration_timestamp_secs", "payload", "signature", "events", "timestamp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        signature: typing.Union[MetaOapg.properties.signature, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        event_root_hash: typing.Union[MetaOapg.properties.event_root_hash, str, ],
        gas_used: typing.Union[MetaOapg.properties.gas_used, str, ],
        changes: typing.Union[MetaOapg.properties.changes, list, tuple, ],
        state_checkpoint_hash: typing.Union[MetaOapg.properties.state_checkpoint_hash, str, ],
        state_change_hash: typing.Union[MetaOapg.properties.state_change_hash, str, ],
        accumulator_root_hash: typing.Union[MetaOapg.properties.accumulator_root_hash, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        version: typing.Union[MetaOapg.properties.version, str, ],
        expiration_timestamp_secs: typing.Union[MetaOapg.properties.expiration_timestamp_secs, str, ],
        sequence_number: typing.Union[MetaOapg.properties.sequence_number, str, ],
        vm_status: typing.Union[MetaOapg.properties.vm_status, str, ],
        payload: typing.Union[MetaOapg.properties.payload, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        sender: typing.Union[MetaOapg.properties.sender, str, ],
        success: typing.Union[MetaOapg.properties.success, bool, ],
        gas_unit_price: typing.Union[MetaOapg.properties.gas_unit_price, str, ],
        max_gas_amount: typing.Union[MetaOapg.properties.max_gas_amount, str, ],
        events: typing.Union[MetaOapg.properties.events, list, tuple, ],
        hash: typing.Union[MetaOapg.properties.hash, str, ],
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserTransaction':
        return super().__new__(
            cls,
            *args,
            signature=signature,
            event_root_hash=event_root_hash,
            gas_used=gas_used,
            changes=changes,
            state_checkpoint_hash=state_checkpoint_hash,
            state_change_hash=state_change_hash,
            accumulator_root_hash=accumulator_root_hash,
            type=type,
            version=version,
            expiration_timestamp_secs=expiration_timestamp_secs,
            sequence_number=sequence_number,
            vm_status=vm_status,
            payload=payload,
            sender=sender,
            success=success,
            gas_unit_price=gas_unit_price,
            max_gas_amount=max_gas_amount,
            events=events,
            hash=hash,
            timestamp=timestamp,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_aptos_api.model.delete_module_change import DeleteModuleChange
from openapi_aptos_api.model.delete_resource_change import DeleteResourceChange
from openapi_aptos_api.model.delete_table_item_change import DeleteTableItemChange
from openapi_aptos_api.model.ed25519_signature_request import Ed25519SignatureRequest
from openapi_aptos_api.model.entry_function_payload_request import EntryFunctionPayloadRequest
from openapi_aptos_api.model.module_bundle_payload_request import ModuleBundlePayloadRequest
from openapi_aptos_api.model.multi_agent_signature_request import MultiAgentSignatureRequest
from openapi_aptos_api.model.multi_ed25519_signature_request import MultiEd25519SignatureRequest
from openapi_aptos_api.model.script_payload_request import ScriptPayloadRequest
from openapi_aptos_api.model.transaction_event import TransactionEvent
from openapi_aptos_api.model.write_or_update_module_change import WriteOrUpdateModuleChange
from openapi_aptos_api.model.write_resource_change import WriteResourceChange
from openapi_aptos_api.model.write_table_change_set_change import WriteTableChangeSetChange
