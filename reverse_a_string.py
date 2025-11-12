import string

#reversing using slicing
user_string = input("Enter a string to be reversed: \n")

def reverse_string(user_string):
    reversed_string = user_string[::-1]
    print(f"A string reversed using slicing: {reversed_string}\n")

reverse_string(user_string)

#reversing using for loop
user_string_for_loop = input("Enter a second string to be reversed: \n")

def reverse_string_for_loop(user_string_for_loop):
    reversed_for_loop = ''
    for char in user_string_for_loop:
        reversed_for_loop = char + reversed_for_loop
    print(f"A string reversed using a for loop: {reversed_for_loop}\n")

reverse_string_for_loop(user_string_for_loop)

#ignoring whitespace or punctionation (imported string for punctuation)
user_long_string = input(f"Enter a sentence to be reversed with punctuation: \n")

def reverse_string_without_spaces(user_long_string):
    string_without_spaces = user_long_string.replace(" ", "").replace("\n", "")
    translator = str.maketrans('', '', string.punctuation)
    string_without_punctuation = string_without_spaces.translate(translator)

    reversed_clean_string = string_without_punctuation[::-1]
    print(f"This is a sentence without spaces or punctuation: {reversed_clean_string}\n")

reverse_string_without_spaces(user_long_string)

#lists as well
user_list_to_be_reversed = input("Input a list separated by commas: \n")

def reverse_list(user_list_to_be_reversed):
    sanitized_user_list = [s.strip() for s in user_list_to_be_reversed.split(',')][::-1]
    print(sanitized_user_list)

reverse_list(user_list_to_be_reversed)