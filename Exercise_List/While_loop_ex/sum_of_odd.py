number=int(input("Enter Number : "))
n=1
sum=0
while(n<=number):
    if n%2!=0:
        sum=sum+n
    n+=1
print(f"sum of Odd numbers is {sum}")