# Python program to find the greatest of three numbers

# Taking input from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

# Determining the greatest number
if x > y and x > z:
    print("Greatest number =", x)
elif y > z:
    print("Greatest number =", y)
else:
    print("Greatest number =", z)
