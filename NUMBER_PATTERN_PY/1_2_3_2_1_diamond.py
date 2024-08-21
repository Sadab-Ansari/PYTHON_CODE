n = int(input("Enter a number: "))
x = 1

# Upper part
for i in range(n-1):
    for j in range(i, n):  # Leading spaces
        print(" ", end=" ")
    for j in range(i):  # Print x with no space at the end
        print(x, end=" ")
    for j in range(i+1):  # Print x and increment
        print(x, end=" ")
        x += 1
    print()

# Lower part
for i in range(n):
    for j in range(i+1):  # Leading spaces
        print(" ", end=" ")
    for j in range(i, n-1):  # Print x without decrement initially
        print(x, end=" ")
    for j in range(i, n):  # Print x and decrement
        print(x, end=" ")
        x -= 1
    print()
