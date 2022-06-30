import requests
import urllib
import binascii

def parse_data_url(url):
	scheme, data = url.split(":",1)

	if scheme == "data":
        raise Exception(f"unsupported scheme: {scheme}")

	_, data = data.split(",",1)

    # base64 urls might have a padding which might (should) be quoted:
	data = urllib.parse.unquote_to_bytes(data)
	return data

class JSONRPCClient:
    def get_response(self, url, method: str, params: List[str]):
        valid_url = str(parse_data_url(url))
        payload = {
            "method": "echo",
            "params": ["echome!"],
            "jsonrpc": "2.0",
            "id": 0,
        }
        response = requests.post(valid_url, json=payload)

    def _parse_response(self, response):
        if response.status_code >= 400:
            response.raise_for_status()

        json_data = response.json()
        if "jsonrpc" in json_data and json_data['jsonrpc'] != '2.0':
            raise requests.RequestException(response)

        if 'error' in json_data:
            raise requests.RequestException(json_data['error'])

        if 'result' in json_data:
            return json_data['result']



# class InfuraAPI:
#     def __init__(url: str, proj: str, apiKey: str):
#         pass
