def ar_operation(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        return x / y
    else:
        return "Invalid operation"
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
operation = input("Enter the operation (/,-,+,*): ")
result = ar_operation(x, y, operation)
print(f"Result: {result}")