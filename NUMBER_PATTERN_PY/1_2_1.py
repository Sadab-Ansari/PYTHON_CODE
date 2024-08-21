# 1
# 22
# 111
# 2222
# 11111

n=int(input("Enter a number of rows:" ))
# x=int(input("Enter a number from where you want to start increasing:" ))
for i in range(n):  
    for j in  range(i+1): 
        if(i%2==0):
            print("1",end=" ")
        else:
            print("2", end=" ") 
    print()