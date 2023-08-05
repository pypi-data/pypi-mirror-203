# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

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

from openapi_streams import schemas  # noqa: F401


class AptosCreateStreamType(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "description",
            "tag",
            "webhookUrl",
            "network",
        }
        
        class properties:
            webhookUrl = schemas.StrSchema
            tag = schemas.StrSchema
        
            @staticmethod
            def network() -> typing.Type['AptosNetwork']:
                return AptosNetwork
            description = schemas.StrSchema
            
            
            class functions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'functions':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class events(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'events':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            includePayload = schemas.BoolSchema
            includeEvents = schemas.BoolSchema
            includeChanges = schemas.BoolSchema
            demo = schemas.BoolSchema
            allAddresses = schemas.BoolSchema
            __annotations__ = {
                "webhookUrl": webhookUrl,
                "tag": tag,
                "network": network,
                "description": description,
                "functions": functions,
                "events": events,
                "includePayload": includePayload,
                "includeEvents": includeEvents,
                "includeChanges": includeChanges,
                "demo": demo,
                "allAddresses": allAddresses,
            }
    
    description: MetaOapg.properties.description
    tag: MetaOapg.properties.tag
    webhookUrl: MetaOapg.properties.webhookUrl
    network: 'AptosNetwork'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> 'AptosNetwork': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functions"]) -> MetaOapg.properties.functions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["events"]) -> MetaOapg.properties.events: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includePayload"]) -> MetaOapg.properties.includePayload: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeEvents"]) -> MetaOapg.properties.includeEvents: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeChanges"]) -> MetaOapg.properties.includeChanges: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["demo"]) -> MetaOapg.properties.demo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allAddresses"]) -> MetaOapg.properties.allAddresses: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["webhookUrl", "tag", "network", "description", "functions", "events", "includePayload", "includeEvents", "includeChanges", "demo", "allAddresses", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["webhookUrl"]) -> MetaOapg.properties.webhookUrl: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tag"]) -> MetaOapg.properties.tag: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> 'AptosNetwork': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functions"]) -> typing.Union[MetaOapg.properties.functions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["events"]) -> typing.Union[MetaOapg.properties.events, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includePayload"]) -> typing.Union[MetaOapg.properties.includePayload, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeEvents"]) -> typing.Union[MetaOapg.properties.includeEvents, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeChanges"]) -> typing.Union[MetaOapg.properties.includeChanges, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["demo"]) -> typing.Union[MetaOapg.properties.demo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allAddresses"]) -> typing.Union[MetaOapg.properties.allAddresses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["webhookUrl", "tag", "network", "description", "functions", "events", "includePayload", "includeEvents", "includeChanges", "demo", "allAddresses", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        tag: typing.Union[MetaOapg.properties.tag, str, ],
        webhookUrl: typing.Union[MetaOapg.properties.webhookUrl, str, ],
        network: 'AptosNetwork',
        functions: typing.Union[MetaOapg.properties.functions, list, tuple, schemas.Unset] = schemas.unset,
        events: typing.Union[MetaOapg.properties.events, list, tuple, schemas.Unset] = schemas.unset,
        includePayload: typing.Union[MetaOapg.properties.includePayload, bool, schemas.Unset] = schemas.unset,
        includeEvents: typing.Union[MetaOapg.properties.includeEvents, bool, schemas.Unset] = schemas.unset,
        includeChanges: typing.Union[MetaOapg.properties.includeChanges, bool, schemas.Unset] = schemas.unset,
        demo: typing.Union[MetaOapg.properties.demo, bool, schemas.Unset] = schemas.unset,
        allAddresses: typing.Union[MetaOapg.properties.allAddresses, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AptosCreateStreamType':
        return super().__new__(
            cls,
            *args,
            description=description,
            tag=tag,
            webhookUrl=webhookUrl,
            network=network,
            functions=functions,
            events=events,
            includePayload=includePayload,
            includeEvents=includeEvents,
            includeChanges=includeChanges,
            demo=demo,
            allAddresses=allAddresses,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_streams.model.aptos_network import AptosNetwork
