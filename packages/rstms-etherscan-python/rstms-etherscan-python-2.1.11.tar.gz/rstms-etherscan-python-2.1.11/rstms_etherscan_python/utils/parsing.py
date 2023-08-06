import requests

from ..exceptions import (
    EtherscanErrorResponse,
    EtherscanStatusFailure,
    EtherscanUnauthorizedEndpoint,
    EtherscanUnexpectedResponse,
)

PRO_ENDPOINT_RESPONSE = (
    "Sorry, it looks like you are trying to access an API Pro endpoint. Contact us to upgrade to API Pro."
)


class ResponseParser:
    @staticmethod
    def parse(response: requests.Response):
        content = response.json()
        if "result" in content.keys():
            result = content["result"]
        elif "error" in content.keys():
            raise EtherscanErrorResponse(f"response={content}")
        else:
            raise EtherscanUnexpectedResponse(f"response={content}")
        if "status" in content.keys():
            status = bool(int(content["status"]))
            if result == PRO_ENDPOINT_RESPONSE:
                url, _, _ = response.url.partition("apikey=")
                url += "apikey=..."
                raise EtherscanUnauthorizedEndpoint(f"{result} {url=}")
            if status is None:
                raise EtherscanStatusFailure(f"response={content}")
        else:
            # GETH or Parity proxy msg format
            result = dict(jsonrpc=content["jsonrpc"], cid=int(content["id"]), result=result)
        return result
