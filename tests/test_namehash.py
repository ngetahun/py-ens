import pytest

from py_ens.namehash import namehash


@pytest.mark.parametrize(
    "hash_value, expected_result",
    [
        ("", "0000000000000000000000000000000000000000000000000000000000000000"),
        ("eth", "93cdeb708b7545dc668eb9280176169d1c33cfd8ed6f04690a0bcc88a93fc4ae"),
        ("foo.eth", "de9b09fd7c5f901e23a3f19fecc54828e9c848539801e86591bd9801b019f84f"),
    ],
)
def test_Namehash(hash_value, expected_result):
    assert namehash(hash_value) == expected_result
