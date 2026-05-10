def count_divisors(num):
    count = 0
    for div in range(1, num + 1):
        if num % div == 0:
            count += 1
    return count
