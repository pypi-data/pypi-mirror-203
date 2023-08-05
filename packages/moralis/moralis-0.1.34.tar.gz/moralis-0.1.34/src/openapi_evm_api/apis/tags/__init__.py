# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_evm_api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    BALANCE = "balance"
    BLOCK = "block"
    DEFAULT = "default"
    DEFI = "defi"
    EVENTS = "events"
    IPFS = "ipfs"
    NFT = "nft"
    RESOLVE = "resolve"
    TOKEN = "token"
    TRANSACTION = "transaction"
    UTILS = "utils"
