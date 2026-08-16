#Fibonacci 0 1 1 2 3 5 8 13 21 34 
num=10
a=0
b=1
for i in range(num):
    print(a,end=" ")
    res=a + b
    a=b
    b=res
