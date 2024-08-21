x=int(input("Enter the fist number:"))
y=int(input("Enter the second number:"))
z=int(input("Enter the third number:"))

if(x>y and x>z):
    print(f"{x} is the greatest number among {x},{y} and {z}")

elif(y>z):
    print(f"{y} is the greatest number among {x},{y} and {z}")

else:
    print(f"{z} is the greatest number among {x},{y} and {z}")
