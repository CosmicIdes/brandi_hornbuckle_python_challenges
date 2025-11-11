list_of_numbers = input("Enter a list of numbers separated by commas: \n")

def find_max(list_of_numbers):

    try:
        sanitized_input = [int(n.strip()) for n in list_of_numbers.split(',')]
    except Exception as e:
        print(f"{e}: Please enter a list of numbers in integer form. \n")
    else:
        max_number = sanitized_input[0]
        max_index = 0
        for index, number in enumerate(sanitized_input):
            if number > max_number:
                max_number = number
                max_index = index

        return max_number, max_index   

max_number_found = find_max(list_of_numbers)
    
print(f"The max number in the list and its index is {max_number_found}. \n")


def find_max_while_loop(list_of_numbers):
    try:
        sanitized_while_input = [int(n.strip()) for n in list_of_numbers.split(',')]
    except Exception as e:
        print(f"{e}: Please enter a list of numbers in integer form. \n")
    else:
        while_number = sanitized_while_input[0]
        max_while_number = sanitized_while_input[while_number]
        max_while_index = 0
        while max_while_number < len(sanitized_while_input):
            if sanitized_while_input[while_number] > max_while_number:
                max_while_number = sanitized_while_input[while_number]
            while_number = while_number+1
            max_while_index = max_while_index+1

        return max_while_number, max_while_index

max_while_number_found = find_max_while_loop(list_of_numbers)

print(f"The max number in the while list and its index is {max_while_number_found} \n")