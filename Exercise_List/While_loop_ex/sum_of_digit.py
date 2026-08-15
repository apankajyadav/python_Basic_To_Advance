#find and print sum of digit of the given number .
num=int(input("Enter Number you want to calculate sum of digit: "))
sum=0
while(num>0):
    digit=num % 10
    sum=sum + digit
    num=num // 10 
print(f"Sum of Enter digit nunber is {sum}")