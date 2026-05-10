def sum_odd_digits(n):
    total = 0
    for digit in str(abs(num)):
        if int(digit) % 2 != 0:
            total += int(digit)
    return total
