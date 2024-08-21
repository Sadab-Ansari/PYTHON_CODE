num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result of addition:", num1 + num2)
elif choice == 2:
    print("Result of subtraction:", num1 - num2)
elif choice == 3:
    print("Result of multiplication:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result of division:", num1 / num2)
    else:
        print("Error! Division by zero is not allowed.")
else:
    print("Invalid choice! Please select a valid operation.")
