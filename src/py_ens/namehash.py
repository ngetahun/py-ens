from eth_hash.auto import keccak as keccak_256
from eth_utils import decode_hex, encode_hex, remove_0x_prefix
from idna import encode

EMPTY = remove_0x_prefix(encode_hex("\0" * 32))


def namehash(_name: str):
    if _name == "":
        return EMPTY

    res = EMPTY
    parts = []
    try:
        parts = _name.split(".")
    except ValueError:
        parts = [_name]

    parts.reverse()
    for part in parts:
        _h = remove_0x_prefix(encode_hex(keccak_256(_normalize(part))))
        res += _h
        res = remove_0x_prefix(encode_hex(keccak_256(decode_hex(res))))
    return res


def _normalize(_unencoded_name: str) -> str:
    # Perform UTS46 compatible normalization
    return encode(_unencoded_name, uts46=True, transitional=False)
