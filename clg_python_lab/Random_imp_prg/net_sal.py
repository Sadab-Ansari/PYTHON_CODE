n=int(input("Enter a basic salary"))
def net_sal(n):
    hra=(20*n)/100
    da=(60*n)/100
    net_sal=n+hra+da
    print("Net salary",net_sal)
net_sal(n)