# coding: utf-8

"""
    aptos-api

    The aptos-api provider  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from openapi_aptos_api.paths.nfts_collections_collection_data_id_hash_owners.get import GetNftOwnersByCollection
from openapi_aptos_api.paths.nfts_owners.get import GetNftOwnersByTokens
from openapi_aptos_api.paths.nfts_collections_collection_data_id_hash_owners_list.get import GetNftOwnersOfCollection
from openapi_aptos_api.paths.nfts_transfers_collections_collection_data_id_hash.get import GetNftTransfersByCollection
from openapi_aptos_api.paths.nfts_transfers_creators.get import GetNftTransfersByCreators
from openapi_aptos_api.paths.nfts_transfers.get import GetNftTransfersByIds
from openapi_aptos_api.paths.nfts_transfers_wallets.get import GetNftTransfersByWallets
from openapi_aptos_api.paths.nfts_collections_collection_data_id_hash_tokens.get import GetNftsByCollection
from openapi_aptos_api.paths.nfts_creators.get import GetNftsByCreators
from openapi_aptos_api.paths.nfts.get import GetNftsByIds


class NftsApi(
    GetNftOwnersByCollection,
    GetNftOwnersByTokens,
    GetNftOwnersOfCollection,
    GetNftTransfersByCollection,
    GetNftTransfersByCreators,
    GetNftTransfersByIds,
    GetNftTransfersByWallets,
    GetNftsByCollection,
    GetNftsByCreators,
    GetNftsByIds,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
