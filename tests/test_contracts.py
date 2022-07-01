
import pytest
from py_ens.contracts import ENSRegistryContract
from vcr import VCR
from py_ens.clients import JSONRPCClient
from py_ens.namehash import namehash
from py_ens.address import Address

vcr = VCR(
    serializer='yaml',
    cassette_library_dir='tests/fixtures/cassettes',
    record_mode='once',
    match_on=['uri', 'method'],
)

@pytest.mark.xfail
@pytest.mark.vcr
@vcr.use_cassette()
@pytest.mark.parametrize('name_address,resolved_address', [
        ('vitalik.eth', Address('0x4976fb03c32e5b8cfe2b6ccb31c09ba78ebaba41')),
        ('unknownETH', None)
    ])
def test_ENSRegistryContract_empty_resolver_result(name_address, resolved_address):
    client = JSONRPCClient('https://cloudflare-eth.com/') # change this
    contract = ENSRegistryContract(client)
    test_namehash = namehash(name_address)
    result = contract.resolver(test_namehash)
    assert result == resolved_address
