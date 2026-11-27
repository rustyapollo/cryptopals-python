# Encoding and decoding utilities for Cryptopals.

import base64

def hex_to_base64(hex_string: str) -> str:
    # Convert a hexadecimal string to a Base64 string.
    raw_bytes = bytes.fromhex(hex_string)
    return base64.b64encode(raw_bytes).decode("ascii")


def base64_to_hex(base64_string: str) -> str:
    # Convert a Base64 string to a hexadecimal string.
    raw_bytes = base64.b64decode(base64_string)
    return raw_bytes.hex()