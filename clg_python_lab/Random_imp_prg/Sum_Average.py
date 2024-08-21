# Taking input from the user
n = int(input("Enter the number of elements in the array: "))
arr = []

print("Enter the elements in the array:")
for _ in range(n):
    arr.append(int(input()))

# Calculating the sum and average
sum_elements = sum(arr)
average = sum_elements // n  # Use integer division to match Java's behavior

# Printing the results
print("The sum of the elements in the array is:", sum_elements)
print("Average is:", average)
