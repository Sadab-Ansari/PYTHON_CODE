def average(a,b,c):
    # total=a+b+c
    avg=(a+b+c)/3
    return avg

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
x=average(a,b,c)
print(f"The average of three number is {x}")
# average(a,b,c)
# print("The average of three number is ",average(a,b,c))