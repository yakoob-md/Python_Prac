a=0
n=int(input("enter the value of n: "))
b=1
sum=a+b
for i in range(1,n,1):
    a=b
    b=sum
    sum=a+b
    print(sum,sep='   ')