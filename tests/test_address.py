import pytest
from py_ens.address import Address

def test_address_upper_and_lower():
    _hex = "0X5AAEB6053F3E94C9B9A09F33669435E7EF1BEAED"
    address = Address(_hex)

    assert address.hexString() == "0x5aAeb6053F3E94C9b9A09f33669435E7Ef1BeAed"
    assert address.hexString().upper() == "0X5AAEB6053F3E94C9B9A09F33669435E7EF1BEAED"
    assert address.hexString().lower() == "0x5aaeb6053f3e94c9b9a09f33669435e7ef1beaed"


def test_checksum_exceptions():
    illegal_hex = "0xdbF03B407c01E7cD3CbEA99509d93f8DDDC8C6fb"

    with pytest.raises(Exception):
        address = Address(illegal_hex)
