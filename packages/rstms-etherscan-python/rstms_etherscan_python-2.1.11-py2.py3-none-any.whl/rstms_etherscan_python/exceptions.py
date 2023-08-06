# Etherscan API Exceptions


class EtherscanUnauthorizedEndpoint(Exception):
    pass


class EtherscanErrorResponse(Exception):
    pass


class EtherscanStatusFailure(Exception):
    pass


class EtherscanUnexpectedResponse(Exception):
    pass
