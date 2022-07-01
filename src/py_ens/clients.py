import urllib
from typing import List
from eth_utils import to_text
import requests

# TODO: Validate urls

class JSONRPCClient:
    def __init__(self, url):
        self.url = url

    def get_response(self, method: str, params: List[str]):
        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": 1,
        }
        response = requests.post(self.url, json=payload)
        return self._parse_response(response)

    def _parse_response(self, response):
        if response.status_code >= 400:
            response.raise_for_status()

        json_data = response.json()
        if "jsonrpc" in json_data and json_data["jsonrpc"] != "2.0":
            raise requests.RequestException(response)

        if "error" in json_data:
            raise requests.RequestException(json_data["error"])

        if "result" in json_data:
            return json_data["result"], "success"


# class InfuraAPI:
#   def __init__(url: str, proj: str, apiKey: str):
#       pass
