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


class UUID(
    schemas.UUIDSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Stringified UUIDv4.
See [RFC 4112](https://tools.ietf.org/html/rfc4122)
    """


    class MetaOapg:
        format = 'uuid'
        regex=[{
            'pattern': r'[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-4[0-9A-Fa-f]{3}-[89ABab][0-9A-Fa-f]{3}-[0-9A-Fa-f]{12}',  # noqa: E501
        }]
