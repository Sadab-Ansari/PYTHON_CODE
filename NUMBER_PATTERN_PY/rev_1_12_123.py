# 12345
#  1234
#   123
#    12
#     1

n=int(input("Enter a number of rows:" ))
for i in range(n):  
    x=1
    for j in  range(i+1): 
        print(" ",end="") 

    for j in range(i,n):
        print(x,end="")   
        x+=1
    print()