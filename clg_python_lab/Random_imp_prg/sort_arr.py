# Python program to sort an array of five elements using bubble sort

# Initialize an empty list to store the elements
x = []

# Taking input from the user
print("Enter five elements:")
for i in range(5):
    element = int(input())
    x.append(element)

# Performing bubble sort
for i in range(4):
    for j in range(4 - i):
        if x[j] > x[j + 1]:
            # Swap the elements
            x[j], x[j + 1] = x[j + 1], x[j]

# Printing the sorted array
print("Sorted Array:")
for i in range(5):
    print(x[i], end=" ")
