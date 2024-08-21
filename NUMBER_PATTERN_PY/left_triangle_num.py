# 1
# 22
# 333
# 4444
# 55555

n=int(input("Enter a number of rows:" ))
x=int(input("Enter a number from where you want to start:" ))
for i in range(n):  #number of rows
    for j in  range(i+1): #number of columns 
        print( x,end=" ") #printing and  spacing
    x+=1
    print() # next line