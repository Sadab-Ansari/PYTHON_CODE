# Python program to generate a Fibonacci series

# Taking input from the user
n = int(input("Enter the number of terms: "))

# Initializing the first two terms
q = 0
p = 1

# Printing the first two terms of the Fibonacci series
print("The Fibonacci series is:", q, p, end=" ")

# Generating the Fibonacci series
for i in range(3, n + 1):
    c = q + p
    print(c, end=" ")
    q = p
    p = c
