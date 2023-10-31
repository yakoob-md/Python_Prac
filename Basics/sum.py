n=int(input("enter the value of n : "))
# normal sum upto n numbers 
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print(sum,end="\n\n")
# sum of cube of n numbers 
sum1=0
for i in range(1,n+1,1):
    a=i*i*i
    sum1=sum1+a
print(sum1,end='\n\n')
# sum of square of n numbers
sum2=0
for i in range(1,n+1,1):
    b=i*i
    sum2=sum2+b
print(sum2)