# coding: utf-8

"""
    Auth API

    API that provides authentication services for dapps.  # noqa: E501

    The version of the OpenAPI document: 1.0
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

from openapi_auth import schemas  # noqa: F401


class SolanaCompleteChallengeResponseDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "address",
            "profileId",
            "domain",
            "id",
            "nonce",
            "uri",
            "version",
            "network",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 8
                    regex=[{
                        'pattern': r'^[a-zA-Z0-9]{8,64}$',  # noqa: E501
                    }]
            domain = schemas.StrSchema
            uri = schemas.StrSchema
            version = schemas.StrSchema
            nonce = schemas.StrSchema
            profileId = schemas.StrSchema
            
            
            class network(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "mainnet": "MAINNET",
                        "testnet": "TESTNET",
                        "devnet": "DEVNET",
                    }
                
                @schemas.classproperty
                def MAINNET(cls):
                    return cls("mainnet")
                
                @schemas.classproperty
                def TESTNET(cls):
                    return cls("testnet")
                
                @schemas.classproperty
                def DEVNET(cls):
                    return cls("devnet")
            address = schemas.StrSchema
            statement = schemas.StrSchema
            expirationTime = schemas.DateTimeSchema
            notBefore = schemas.DateTimeSchema
            
            
            class resources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'resources':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "domain": domain,
                "uri": uri,
                "version": version,
                "nonce": nonce,
                "profileId": profileId,
                "network": network,
                "address": address,
                "statement": statement,
                "expirationTime": expirationTime,
                "notBefore": notBefore,
                "resources": resources,
            }
    
    address: MetaOapg.properties.address
    profileId: MetaOapg.properties.profileId
    domain: MetaOapg.properties.domain
    id: MetaOapg.properties.id
    nonce: MetaOapg.properties.nonce
    uri: MetaOapg.properties.uri
    version: MetaOapg.properties.version
    network: MetaOapg.properties.network
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileId"]) -> MetaOapg.properties.profileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["network"]) -> MetaOapg.properties.network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statement"]) -> MetaOapg.properties.statement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expirationTime"]) -> MetaOapg.properties.expirationTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notBefore"]) -> MetaOapg.properties.notBefore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> MetaOapg.properties.resources: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "domain", "uri", "version", "nonce", "profileId", "network", "address", "statement", "expirationTime", "notBefore", "resources", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["domain"]) -> MetaOapg.properties.domain: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uri"]) -> MetaOapg.properties.uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nonce"]) -> MetaOapg.properties.nonce: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileId"]) -> MetaOapg.properties.profileId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["network"]) -> MetaOapg.properties.network: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statement"]) -> typing.Union[MetaOapg.properties.statement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expirationTime"]) -> typing.Union[MetaOapg.properties.expirationTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notBefore"]) -> typing.Union[MetaOapg.properties.notBefore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> typing.Union[MetaOapg.properties.resources, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "domain", "uri", "version", "nonce", "profileId", "network", "address", "statement", "expirationTime", "notBefore", "resources", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address: typing.Union[MetaOapg.properties.address, str, ],
        profileId: typing.Union[MetaOapg.properties.profileId, str, ],
        domain: typing.Union[MetaOapg.properties.domain, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        nonce: typing.Union[MetaOapg.properties.nonce, str, ],
        uri: typing.Union[MetaOapg.properties.uri, str, ],
        version: typing.Union[MetaOapg.properties.version, str, ],
        network: typing.Union[MetaOapg.properties.network, str, ],
        statement: typing.Union[MetaOapg.properties.statement, str, schemas.Unset] = schemas.unset,
        expirationTime: typing.Union[MetaOapg.properties.expirationTime, str, datetime, schemas.Unset] = schemas.unset,
        notBefore: typing.Union[MetaOapg.properties.notBefore, str, datetime, schemas.Unset] = schemas.unset,
        resources: typing.Union[MetaOapg.properties.resources, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SolanaCompleteChallengeResponseDto':
        return super().__new__(
            cls,
            *args,
            address=address,
            profileId=profileId,
            domain=domain,
            id=id,
            nonce=nonce,
            uri=uri,
            version=version,
            network=network,
            statement=statement,
            expirationTime=expirationTime,
            notBefore=notBefore,
            resources=resources,
            _configuration=_configuration,
            **kwargs,
        )
