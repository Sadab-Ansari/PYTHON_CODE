# Python program to check if a number is an Armstrong number

# Taking input from the user
n = int(input("Enter any number: "))

# Storing the original number for comparison later
n1 = n
sum = 0

# Calculating the sum of the cubes of the digits
while n1 != 0:
    r = n1 % 10
    sum += r ** 3
    n1 //= 10

# Checking if the sum equals the original number
if sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")
