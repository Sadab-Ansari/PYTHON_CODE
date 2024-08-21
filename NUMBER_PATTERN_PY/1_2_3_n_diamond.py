n=int(input("Enter a number:"))
x=1
for i in range(n-1):  
    for j in  range(i,n): 
        print(" ",end=" ")
    for j in range(i):
        print( x , end="")
    for j in range(i+1):
        print( x , end="")
    x+=1
    print()

for i in range(n):  
    for j in  range(i+1): 
        print(" ",end=" ")
    for j in range(i,n-1):
        print( x , end="")
    for j in range(i,n):
        print( x , end="")
    print()