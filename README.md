# Caesar Cipher Encryption Tool

## Project Overview
This project is a Python-based implementation of the Caesar Cipher, a foundational encryption algorithm. The purpose of this tool was to practice algorithmic logic, character encoding manipulation, and command-line input handling.

## Technical Methodology
* **Algorithmic Logic**: Implemented the cipher using the modulo operator to ensure cyclical wrapping of the alphabet.
* **Character Encoding**: Utilized `ord()` and `chr()` functions to perform ASCII/Unicode value manipulation for character shifting.
* **Modular Design**: Separated encryption logic (`encode_message`) from user interface logic, allowing for cleaner, more readable code.

## Key Features
* **Dynamic Shifting**: Supports any shift amount provided by the user.
* **Case Preservation**: Automatically detects uppercase vs. lowercase characters to maintain proper formatting.
* **Data Sanitization**: Non-alphabetic characters (like spaces or punctuation) are preserved, ensuring the original message structure remains intact.

## Why This Matters in Security
While the Caesar Cipher is not secure by modern cryptographic standards, implementing it from scratch demonstrates a fundamental understanding of how encryption algorithms transform plaintext into ciphertext. This is a core concept when analyzing more complex cryptographic protocols.
