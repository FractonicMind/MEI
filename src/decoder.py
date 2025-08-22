# MIE Decoder
# Decodes a string of MIE expressions back into readable text.

import re

def decode_mie(mie_string: str) -> str:
    """
    Decodes a space-separated string of MIE expressions into text.
    '0' is treated as a binary 0.
    Any other parenthesized expression is treated as a binary 1.
    """
    expressions = mie_string.strip().split(' ')
    binary_string = ""

    for expr in expressions:
        if expr == '0':
            binary_string += '0'
        # A simple check to ensure the expression is in a valid format (e.g., '(...)')
        elif re.match(r'^\(.*\)$', expr):
            binary_string += '1'

    # Convert the full binary string back to text
    text = ""
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        if len(byte) == 8:
            try:
                text += chr(int(byte, 2))
            except ValueError:
                # Handle cases where a byte might not be a valid ASCII character
                text += '?'
    return text

if __name__ == '__main__':
    # An example MIE message for the word "MIE"
    # 01001101 01001001 01000101
    mie_message = "(1) 0 (1) 0 (1) (1) 0 (1) (1) 0 (1) 0 (1) 0 0 (1) (1) 0 (1) 0 0 0 (1) 0 (1)"

    decoded_text = decode_mie(mie_message)
    print(f"MIE Encoded: {mie_message}")
    print(f"Decoded Text: {decoded_text}")
