
# Cryptopals Set 1, Challenge 1: Convert hex to Base64."""

from cryptopals.encoding import hex_to_base64


def main():
    # Run Set 1, Challenge 1.
    hex_input = (
        "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573"
        "206d757368726f6f6d"
    )

    result = hex_to_base64(hex_input)

    print("Cryptopals - Set 1, Challenge 1")
    print(f"Hex input:  {hex_input}")
    print(f"Base64:     {result}")


if __name__ == "__main__":
    main()
