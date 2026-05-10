def binary_to_decimal(binary_str):
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal
