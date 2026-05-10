# 2. Print the reverse of an integer
def reverse_integer(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)
