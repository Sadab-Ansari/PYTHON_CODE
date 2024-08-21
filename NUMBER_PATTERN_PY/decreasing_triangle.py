n=int(input("Enter a number of rows:" ))
x=int(input("Enter a number from where you want to start dicreasing:" ))
for i in range(n):  
    for j in  range(i+1): 
        print( x,end=" ") 
    x-=1
    print()