def count_upper(alpha):
    count = 0
    for char in alpha:
        if char.isupper():
            count += 1
    return count
