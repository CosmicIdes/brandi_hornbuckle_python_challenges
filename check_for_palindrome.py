import string

user_input = input("Enter a word or phrase to check if it is a palindrome: \n")

def is_palindrome(user_input):
    no_space_input = user_input.replace(" ", "").replace("\n", "")
    translator = str.maketrans('', '', string.punctuation)
    normalized_input = no_space_input.translate(translator)
    reversed_normalized_input = normalized_input[::-1]

    if reversed_normalized_input == normalized_input:
        print(f"Yes, {user_input} is a palindrome!")
    else:
        print(f"No, {user_input} is not a palindome. :(")

is_palindrome(user_input)