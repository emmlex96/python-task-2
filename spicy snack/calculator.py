a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print("Can't divide by zero" if b == 0 else a / b)
else:
    print("Invalid operator")
