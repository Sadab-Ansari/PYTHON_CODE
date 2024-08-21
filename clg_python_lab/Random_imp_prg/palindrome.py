n = int(input("Enter any number: "))
n1 = n
r = 0

while n != 0:
    r = r * 10 + n % 10
    n //= 10

if r == n1:
    print(f"{n1} is a palindrome number")
else:
    print(f"{n1} is not a palindrome number")
