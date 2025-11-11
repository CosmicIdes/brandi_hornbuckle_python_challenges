prime_input = input("Please enter a integer: \n")

def is_prime(prime_input):
    try:
        sanitized_input = int(prime_input)
        
        if sanitized_input <= 1: 
            print(False)
        else:
            is_it_prime = True
            for n in range(2, int(sanitized_input**0.5) + 1):
                if sanitized_input % n == 0:
                    is_it_prime = False
                    break
            return is_it_prime
    except Exception as e:
        print(f"{e}: please enter an integer: \n")


result_is_it_prime = is_prime(prime_input)
print(f"Is the number prime? {result_is_it_prime} \n")

#Checking if multiple numbers are prime in one run

prime_multiple_input = input("Enter multiple numbers separated by a comma: \n")

def is_multiple_prime(prime_multiple_input):
    try:
        sanitized_multiple_input = [int(n.strip()) for n in prime_multiple_input.split(',')]
    except Exception as e:
        print(f"{e}: Please enter multiple numbers in integer form. \n")
    else:
        with open("prime_numbers.txt", "w") as file:
            for number in sanitized_multiple_input:
                if is_prime(number):
                    file.write(str(number) + "\n")
                    print(f"{number} is prime.")
                else:
                    print(f"{number} is not prime.")

is_multiple_prime(prime_multiple_input)
