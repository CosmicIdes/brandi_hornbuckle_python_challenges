user_input_string = input("Enter a string: \n")
user_input_number = input("Enter a number to shift by: \n")

def caesar_cipher_encode(user_input_string, user_input_number):
    encoded = ""
    for char in user_input_string:
        if char.isalpha():
            start = ord('a') if char.islower() else ord ('A')
            move_position = (ord(char) - start + int(user_input_number)) % 26
            encoded += chr(start + move_position)
        else:
            encoded += char
    return encoded

encoded_result = caesar_cipher_encode(user_input_string, user_input_number)
print(f"You entered {user_input_string} so your encoded message is: \n {encoded_result}")

user_input_decrypt_string = input("Enter a string to decrypt: \n")
user_input_decrypt_number = input("Enter a number to shift by: \n")

def caesar_ciper_decode(user_input_decrypt_string, user_input_decrypt_number):
    decoded = ""
    for char2 in user_input_decrypt_string:
        if char2.isalpha():
            start2 = ord('a') if char2.islower() else ord('A')
            move_position2 = (ord(char2) - start2 - int(user_input_decrypt_number) + 26) % 26
            decoded += chr(start2 + move_position2)
        else:
            decoded += char2
    return decoded

decoded_result = caesar_ciper_decode(user_input_decrypt_string, user_input_decrypt_number)
print(f"You entered {user_input_decrypt_string} so your decoded message is: \n {decoded_result}")