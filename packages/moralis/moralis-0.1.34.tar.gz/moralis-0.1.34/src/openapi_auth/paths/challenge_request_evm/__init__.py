# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_auth.paths.challenge_request_evm import Api

from openapi_auth.paths import PathValues

path = PathValues.CHALLENGE_REQUEST_EVM