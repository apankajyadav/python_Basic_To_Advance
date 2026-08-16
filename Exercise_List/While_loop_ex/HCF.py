num1=2
num2=10

temp=1
hcf=1

while(temp<=num1 and temp<=num2):
    if num1 % temp == 0 and num2 % temp ==0:
        hcf=temp
    temp+=1
print(hcf)