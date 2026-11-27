import pytest

from cryptopals.encoding import hex_to_base64, base64_to_hex


def assert_hex_to_base64(hex_input, expected):
    assert hex_to_base64(hex_input) == expected


def test_hex_to_base64():
    test_cases = [
        # Cryptopals Set 1, Challenge 1 — official example
        (
            "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573"
            "206d757368726f6f6d",
            "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",
        ),

        # Additional test cases
        ("", ""),
        ("00", "AA=="),
        ("ff", "/w=="),
        ("6869", "aGk="),
        ("48656c6c6f", "SGVsbG8="),
        ("4d616e", "TWFu"),
        ("4d61", "TWE="),
        ("4d", "TQ=="),
        ("000102", "AAEC"),
        ("deadbeef", "3q2+7w=="),
    ]

    total = len(test_cases)

    for number, (hex_input, expected) in enumerate(test_cases, start=1):
        print(f"\nRunning test {number} of {total}: Hex input {hex_input!r}")
        assert_hex_to_base64(hex_input, expected)


def test_base64_to_hex():
    test_cases = [
        ("", ""),
        ("AA==", "00"),
        ("/w==", "ff"),
        ("aGk=", "6869"),
        ("SGVsbG8=", "48656c6c6f"),
        ("TWFu", "4d616e"),
        ("TWE=", "4d61"),
        ("TQ==", "4d"),
        ("AAEC", "000102"),
        ("3q2+7w==", "deadbeef"),
    ]

    total = len(test_cases)

    for number, (base64_input, expected) in enumerate(test_cases, start=1):
        print(f"\nRunning test {number} of {total}: Base64 input {base64_input!r}")
        assert base64_to_hex(base64_input) == expected
