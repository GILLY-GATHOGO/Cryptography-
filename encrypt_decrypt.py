# Plain text
import random

msg = "Hello world how are you doing today"
# Define Encryption level
encryption_level = 128 // 8       # 16 bytes

# Character pool for every bit possible combination
char_pool = ''
for i in range(0x00, 0x255):
    char_pool += chr(i)
# print(char_pool)      This is just for testing

# Generate Key
key = ''
for i in range(encryption_level):
    key += random.choice(char_pool)
print(f' Encryption Key: {key}')

# These variables stores character loops in the string as they are picked one at a time from index 0 to the 15.
key_index = 0
max_key_index = encryption_level - 1

# lets encrypt the message
encrypted_message = ''      # define variable to store the encrypted message

for char in msg:            # Take every character and XOR it with the Key value
    encrypted_char = ord(char) ^ ord(key[key_index])     # The ord variable converts string character int ASCII value
    encrypted_message += chr(encrypted_char)             # Chr converts the integer back to string char
    if key_index >= max_key_index:                       # When it reaches the Max,reset to 0 and increment by 1
        key_index = 0
    else:
        key_index += 1
print(f' Plain Text:  {msg}')
print(f'Encrypted Message:  {encrypted_message}')

# Lets Decrypt the Message
key_index = 0
decrypted_message = ''
for char in encrypted_message:
    decrypted_char = ord(char) ^ ord(key[key_index])
    decrypted_message += chr(decrypted_char)
    # The Incrementer
    if key_index >= max_key_index:  # When it reaches the Max,reset to 0 and increment by 1
        key_index = 0
    else:
        key_index += 1
print(f'Decrypted Message : {decrypted_message}')













