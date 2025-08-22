# A simple MIE Encoder
# Encodes a string into MIE format (0s and expressions that equal 1)
# NOTE: This is a basic example and uses a limited set of expressions for '1'

def to_binary(text):
    """Converts text to an 8-bit binary string."""
    return ''.join(format(ord(char), '08b') for char in text)

def encode_mie(text):
    """Encodes a string into a list of MIE expressions."""
    binary_string = to_binary(text)
    mie_code = []

    for bit in binary_string:
        if bit == '0':
            mie_code.append('0')
        else:
            # For simplicity, we use a single expression for '1'
            mie_code.append('(1+1-1)') 
    return ' '.join(mie_code)

if __name__ == '__main__':
    message = "Lev"
    mie_message = encode_mie(message)
    print(f"Original Text: {message}")
    print(f"MIE Encoded: {mie_message}")
