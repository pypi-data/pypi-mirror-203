# coding: utf-8

"""
    Streams Api

    API that provides access to Moralis Streams  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from openapi_streams.paths.streams_evm_id_address.post import AddAddressToStream
from openapi_streams.paths.streams_evm.put import CreateStream
from openapi_streams.paths.streams_evm_id_address.delete import DeleteAddressFromStream
from openapi_streams.paths.streams_evm_id.delete import DeleteStream
from openapi_streams.paths.streams_evm_id_address.get import GetAddresses
from openapi_streams.paths.streams_evm_id.get import GetStream
from openapi_streams.paths.streams_evm.get import GetStreams
from openapi_streams.paths.streams_evm_id.post import UpdateStream
from openapi_streams.paths.streams_evm_id_status.post import UpdateStreamStatus


class EvmStreamsApi(
    AddAddressToStream,
    CreateStream,
    DeleteAddressFromStream,
    DeleteStream,
    GetAddresses,
    GetStream,
    GetStreams,
    UpdateStream,
    UpdateStreamStatus,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
