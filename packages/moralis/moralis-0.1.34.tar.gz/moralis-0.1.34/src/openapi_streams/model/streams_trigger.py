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


class StreamsTrigger(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Trigger
    """


    class MetaOapg:
        required = {
            "contractAddress",
            "functionAbi",
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "tx": "TX",
                        "log": "LOG",
                        "erc20transfer": "ERC20TRANSFER",
                        "erc20approval": "ERC20APPROVAL",
                        "nfttransfer": "NFTTRANSFER",
                    }
                
                @schemas.classproperty
                def TX(cls):
                    return cls("tx")
                
                @schemas.classproperty
                def LOG(cls):
                    return cls("log")
                
                @schemas.classproperty
                def ERC20TRANSFER(cls):
                    return cls("erc20transfer")
                
                @schemas.classproperty
                def ERC20APPROVAL(cls):
                    return cls("erc20approval")
                
                @schemas.classproperty
                def NFTTRANSFER(cls):
                    return cls("nfttransfer")
            contractAddress = schemas.StrSchema
        
            @staticmethod
            def functionAbi() -> typing.Type['AbiItem']:
                return AbiItem
            
            
            class inputs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            any_of_0 = schemas.StrSchema
                            
                            
                            class any_of_1(
                                schemas.ListSchema
                            ):
                            
                            
                                class MetaOapg:
                                    items = schemas.AnyTypeSchema
                            
                                def __new__(
                                    cls,
                                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                ) -> 'any_of_1':
                                    return super().__new__(
                                        cls,
                                        arg,
                                        _configuration=_configuration,
                                    )
                            
                                def __getitem__(self, i: int) -> MetaOapg.items:
                                    return super().__getitem__(i)
                            
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
                                    cls.any_of_0,
                                    cls.any_of_1,
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
                ) -> 'inputs':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            topic0 = schemas.StrSchema
            callFrom = schemas.StrSchema
            __annotations__ = {
                "type": type,
                "contractAddress": contractAddress,
                "functionAbi": functionAbi,
                "inputs": inputs,
                "topic0": topic0,
                "callFrom": callFrom,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    contractAddress: MetaOapg.properties.contractAddress
    functionAbi: 'AbiItem'
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractAddress"]) -> MetaOapg.properties.contractAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["functionAbi"]) -> 'AbiItem': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputs"]) -> MetaOapg.properties.inputs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["topic0"]) -> MetaOapg.properties.topic0: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["callFrom"]) -> MetaOapg.properties.callFrom: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["contractAddress"], typing_extensions.Literal["functionAbi"], typing_extensions.Literal["type"], typing_extensions.Literal["inputs"], typing_extensions.Literal["topic0"], typing_extensions.Literal["callFrom"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractAddress"]) -> MetaOapg.properties.contractAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["functionAbi"]) -> 'AbiItem': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputs"]) -> typing.Union[MetaOapg.properties.inputs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["topic0"]) -> typing.Union[MetaOapg.properties.topic0, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["callFrom"]) -> typing.Union[MetaOapg.properties.callFrom, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["contractAddress"], typing_extensions.Literal["functionAbi"], typing_extensions.Literal["type"], typing_extensions.Literal["inputs"], typing_extensions.Literal["topic0"], typing_extensions.Literal["callFrom"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        contractAddress: typing.Union[MetaOapg.properties.contractAddress, str, ],
        functionAbi: 'AbiItem',
        type: typing.Union[MetaOapg.properties.type, str, ],
        inputs: typing.Union[MetaOapg.properties.inputs, list, tuple, schemas.Unset] = schemas.unset,
        topic0: typing.Union[MetaOapg.properties.topic0, str, schemas.Unset] = schemas.unset,
        callFrom: typing.Union[MetaOapg.properties.callFrom, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'StreamsTrigger':
        return super().__new__(
            cls,
            *args,
            contractAddress=contractAddress,
            functionAbi=functionAbi,
            type=type,
            inputs=inputs,
            topic0=topic0,
            callFrom=callFrom,
            _configuration=_configuration,
        )

from openapi_streams.model.abi_item import AbiItem
