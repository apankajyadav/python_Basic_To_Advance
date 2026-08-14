num=int(input("Enter Number: "))
a=0
b=1
sum=0
while(num>0):
    sum=sum+a
    a, b = b, a + b
    num-=1
print(sum)


