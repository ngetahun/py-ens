import json
from py_ens.clients import JSONRPCClient
from py_ens.address import Address
from eth_utils import add_0x_prefix
from typing import Optional

def suffix_padded_bytes(d: bytes):
    return d + '\0' * (32 - len(d))


class ContractInterface:
    def __init__(self, client: JSONRPCClient, address: Address):
        self.client = client
        self.address = address

    def _eth_call(self, data):
        # import pdb; pdb.set_trace()
        params = [{
            'to': self.address.hexString().lower(),
            'data': data
        }, 'latest']

        try:
            return self.client.get_response('eth_call', params)
        except:
            raise

    @property
    def null_address(self):
        return Address("0x0000000000000000000000000000000000000000")

    def resolver(self, resolve: Address) -> Optional[Address]:
        raise Exception('Function not implemented!')

    def is_null_address(self, add: Address) -> bool:
        return add == self.null_address


class ENSRegistryContract(ContractInterface):
    registry_address = "0x00000000000C2E074eC69A0dFb2997BA6C7d2e1e"
    interface = {
        'resolver': '0178b8bf'
    }

    def __init__(self, client: JSONRPCClient):
        addr = Address(self.registry_address)
        super(ENSRegistryContract, self).__init__(client, addr)


    def resolver(self, name: str) -> Optional[Address]:
        data = add_0x_prefix(self.interface['resolver'] + suffix_padded_bytes(name))
        res = self._eth_call(data)

        try:
            resolved_address = Address(res)
            if not self.is_null_address(resolved_address):
                return resolved_address
            else:
                return None
        except:
            pass

        return None
