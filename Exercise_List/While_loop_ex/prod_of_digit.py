number=int(input("Enter Number : "))
prod=1
while(number>0):
    digit =number % 10
    prod=prod * digit
    number=number//10
print(f"Product of Enter diigt is : {prod}")