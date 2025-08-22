# A simple script to demonstrate MIE encoding.

import sys
# The sys.path.insert adds the parent directory (the root of the repo)
# to the Python path, allowing us to import from the 'src' folder.
sys.path.insert(0, '../') 

from src.encoder import encode_mie

def main():
    """Encodes a sample message using the MIE encoder."""
    
    # The message we want to encode.
    message = "Hello, MIE!"
    
    # Call the encoder function.
    encoded_message = encode_mie(message)
    
    print(f"Original Text: {message}")
    print(f"MIE Encoded Message: {encoded_message}")

if __name__ == "__main__":
    main()
