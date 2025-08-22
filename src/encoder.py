# MIE Encoder
# Encodes a string of text into the MIE format.

import random

def to_binary_string(text: str) -> str:
    """Converts a string of text into its 8-bit binary representation."""
    return ''.join(format(ord(char), '08b') for char in text)

def get_random_one_expression() -> str:
    """Returns a random mathematical expression that equals 1."""
    expressions = [
        '(1*1)', '(2-1)', '(7/7)', '(9-8)', '(1**9)', '(cos(0))', '(0!+0)'
    ]
    return random.choice(expressions)

def encode_mie(text: str) -> str:
    """
    Encodes a string of text into a space-separated MIE string.
    '0' is represented by '0'.
    '1' is represented by a random mathematical identity for '1'.
    """
    binary_string = to_binary_string(text)
    mie_expressions = []

    for bit in binary_string:
        if bit == '0':
            mie_expressions.append('0')
        else:
            mie_expressions.append(get_random_one_expression())

    return ' '.join(mie_expressions)

if __name__ == '__main__':
    message = "MIE"
    encoded_message = encode_mie(message)
    print(f"Original message: {message}")
    print(f"Encoded MIE string: {encoded_message}")
