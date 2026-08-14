n=int(input("Enter n Vlaue to find Fibonacic: "))
a=0
b=1
count=0
while(count<n):
    print(a," ")
    temp=a+b
    a=b
    b=temp
    count+=1
