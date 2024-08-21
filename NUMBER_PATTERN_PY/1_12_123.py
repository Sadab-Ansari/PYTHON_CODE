# 1
# 12
# 123
# 1234
# 12345
n=int(input("Enter a number of rows:" ))
for i in range(n):  
    x=1
    for j in  range(i+1): 
        print( x ,end=" ") 
        x+=1
    print()