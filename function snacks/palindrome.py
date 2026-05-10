import math

# PSEUDOCODE:
# Define function is_palindrome(number)
#   If number is not a positive integer >= 2 → return False
#   Check palindrome: compare number string to its reverse
#   Check prime:
#       If number == 2 
#       If even  not prime
#       Loop from 3 to sqrt(number): if divisible  not prime
#   Return True only if BOTH palindrome and prime

def is_palindrome(number):
    if not isinstance(number, int) or number < 2:
        return False

    is_palin = str(number) == str(number)[::-1]

    if number == 2:
        is_prime = True
    elif number % 2 == 0:
        is_prime = False
    else:
        is_prime = True
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                is_prime = False
                break

    return is_palin and is_prime
