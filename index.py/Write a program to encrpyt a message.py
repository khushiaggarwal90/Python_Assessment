# Program to encrypt and decrypt a message
# using Caesar Cipher technique.

# Function for encryption
def encrypt(message, shift):

    encrypted_message = ""

    for char in message:

        if char.isalpha():

            # Checking uppercase letters
            if char.isupper():
                encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)

            # Checking lowercase letters
            else:
                encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted_message += char

    return encrypted_message


# Function for decryption
def decrypt(message, shift):

    return encrypt(message, -shift)


# Taking input from user
message = input("Enter message: ")

shift = int(input("Enter shift value: "))

# Encrypting message
encrypted = encrypt(message, shift)

# Decrypting message
decrypted = decrypt(encrypted, shift)

# Displaying results
print("\nEncrypted Message:", encrypted)

print("Decrypted Message:", decrypted)

# Expected Output
"""
Example Input:
Enter message: HELLO
Enter shift value: 3

Expected Output:
Encrypted Message: KHOOR
Decrypted Message: HELLO
"""