n=int(input("enter the number : "))
a=False
for i in range(2,n,1):
    if(n%i==0):
        a=False
        print("composite")
        break
    else:
        a=True
if(a==True):
    print("prime")
