from typing import Optional
import re
import hashlib
from eth_hash.auto import keccak as keccak_256
from eth_utils import to_checksum_address, is_checksum_address

def calculate_keccak256(str_):
    return keccak_256(str_.encode())

class Address:

    def __init__(self, _hex: str):
        hexAddressMatcher = re.compile(r"^(0[xX])?([0-9a-fA-F]{40})$")
        matches = re.match(hexAddressMatcher, _hex)
        if len(matches.groups()) != 2:
            raise Exception()

        extracted = matches.group(2)
        hexChecksumValidated = str(to_checksum_address(extracted))

        lowerCased, upperCased = False, False
        for ch in _hex:
            lowerCased, upperCased = ch.islower(), ch.isupper()

        isChecksumValid = lowerCased and upperCased

        if isChecksumValid and (extracted != hexChecksumValidated):
            raise Exception("Checksum error occured!")

        self._hex = hexChecksumValidated

    def hexString(self, prefix: Optional[bool] = False) -> str:
        hex_prefix = "0x" if prefix else ""
        return hex_prefix + self._hex
