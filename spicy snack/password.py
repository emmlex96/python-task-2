password = input("Enter password: ")
length = len(password)

if length < 1:
    print("Invalid")
elif length < 6:
    print("Weak")
elif length <= 10:
    print("Medium")
else:
    print("Strong")
