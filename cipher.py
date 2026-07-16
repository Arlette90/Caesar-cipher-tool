def encode_message(message, shift):
    """Encodes a message using a simple Caesar cipher with a specified shift.
    Only letters are shifted; other characters remain unchanged."""
    encoded_message = ""

    for char in message: # Iterate through each character in the input message
        if char.isalpha():
            base = 65 if char.isupper() else 97 

            new_char = chr(((ord(char) - base + shift) % 26) + base) # Shift the character and wrap around the alphabet using modulo
            encoded_message += new_char

        else: # If the character is not a letter, keep it unchanged
            encoded_message += char

    return encoded_message

if __name__ == "__main__": # This block will execute when the script is run directly
    print("--- Dynamic Caesar Cipher Encoder ---")

    user_message = input("Enter a message to encode: ") # Prompt the user for input

    user_shift = int(input("Enter the shift amount (e.g., 1 to 25): ")) # Prompt the user for the shift amount

    secret_output = encode_message(user_message, user_shift) # Encode the message using the specified shift
    print('\nOriginal Text:', user_message)
    
    print(f"Encoded Text (Shift +{user_shift}):", secret_output) # Display the original and encoded messages to the user
