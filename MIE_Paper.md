# Mathematical Identity Encoding (MIE)

A novel steganographic method for hiding information in plain sight.

---

## The Principle

The core of MIE is to encode binary data within a grid of mathematical expressions. The method is based on a simple, elegant rule:

- A binary **'0'** is represented by the digit `0`.
- A binary **'1'** is represented by any mathematical expression that resolves precisely to the value of `1`.

This approach transforms a secret message into a format that appears to be a mathematical exercise or abstract notation.

---

## How to Use the Code

The `src/` folder contains a simple Python **encoder** and **decoder** to demonstrate the concept.

### Encoding a Message

To encode a message, you can use the `encoder.py` script. It will convert a string of text into a sequence of MIE expressions.

```bash
python3 src/encoder.py

Decoding a Message

The decoder.py script can be used to convert an MIE message back into a readable string.
Bash

python3 src/decoder.py

Running the Tests

The tests/ folder contains a full suite of unit tests to verify the functionality of the encoder and decoder. To run the tests, use the following command from the root of the repository:
Bash

python3 -m unittest discover tests/

Potential Applications

This project is a proof of concept for several applications, including:

    Digital Watermarking: Embedding a hidden copyright or signature in a document.

    Creative Authentication: A unique form of CAPTCHA.

    Educational Tools: A gamified way to teach mathematical identities.