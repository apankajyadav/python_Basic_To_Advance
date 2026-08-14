#Riverse the gicen number and print revrese value .
Number=int(input("Enter Number you want to reverse :"))

result=0
while(Number>0):
    Digit=Number % 10
    result=result * 10 + Digit
    Number=Number // 10 
print(result)