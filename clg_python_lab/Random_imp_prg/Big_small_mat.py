# Python program to find the smallest and largest elements in a matrix

# Taking input from the user
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Initializing the matrix
matrix = []

print("Enter the elements of the matrix:")
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input())
        row.append(element)
    matrix.append(row)

# Initialize smallest and largest variables
smallest = float('inf')
largest = float('-inf')

# Finding the smallest and largest elements in the matrix
for i in range(rows):
    for j in range(columns):
        if matrix[i][j] < smallest:
            smallest = matrix[i][j]
        if matrix[i][j] > largest:
            largest = matrix[i][j]

# Printing the smallest and largest elements
print("Smallest element:", smallest)
print("Largest element:", largest)
