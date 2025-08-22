# A script to perform unit tests on the MIE encoder and decoder.

import unittest
import sys
import os

# Add the parent directory to the Python path to import from 'src' folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.encoder import encode_mie
from src.decoder import decode_mie

class TestMIE(unittest.TestCase):

    def test_encode_and_decode_simple_string(self):
        """Tests encoding and decoding a simple string."""
        message = "Lev"
        encoded = encode_mie(message)
        decoded = decode_mie(encoded)
        self.assertEqual(message, decoded)

    def test_encode_and_decode_empty_string(self):
        """Tests encoding and decoding an empty string."""
        message = ""
        encoded = encode_mie(message)
        decoded = decode_mie(encoded)
        self.assertEqual(message, decoded)

    def test_encode_and_decode_with_numbers_and_symbols(self):
        """Tests encoding and decoding a string with numbers and symbols."""
        message = "MIE 123"
        encoded = encode_mie(message)
        decoded = decode_mie(encoded)
        self.assertEqual(message, decoded)

    def test_encode_and_decode_long_string(self):
        """Tests encoding and decoding a long string."""
        message = "This is a longer test message to ensure the system works with longer inputs."
        encoded = encode_mie(message)
        decoded = decode_mie(encoded)
        self.assertEqual(message, decoded)
        
    def test_invalid_mie_input(self):
        """Tests how the decoder handles invalid MIE input."""
        invalid_input = "0 (2-1) 0 (invalid)"
        decoded = decode_mie(invalid_input)
        # The decoder should still return a string, even if parts are unreadable
        self.assertIsInstance(decoded, str)

if __name__ == '__main__':
    unittest.main()
