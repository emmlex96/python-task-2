def count_lower(alpha):
    count = 0
    for char in alpha:
        if char.islower():
            count += 1
    return count
