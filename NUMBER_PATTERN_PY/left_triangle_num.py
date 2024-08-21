# 1
# 22
# 333
# 4444
# 55555

n=int(input("Enter a number of rows:" ))
x=int(input("Enter a number from where you want to start increasing:" ))
for i in range(n):  
    for j in  range(i+1): 
        print( x,end=" ") 
    x+=1
    print()