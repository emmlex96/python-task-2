a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c
print(largest)
