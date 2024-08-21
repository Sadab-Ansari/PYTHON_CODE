# Python program to calculate the factorial of a number

# Taking input from the user
n = int(input("Enter any number: "))

# Initializing variables
r = 1
i = 1

# Calculating factorial using a while loop
while i <= n:
    r *= i
    i += 1

# Printing the factorial
print("Factorial =", r)
