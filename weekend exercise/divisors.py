def print_divisors(num):
    for ave in range(1, num + 1):
        if num % ave == 0:
            print(ave)
