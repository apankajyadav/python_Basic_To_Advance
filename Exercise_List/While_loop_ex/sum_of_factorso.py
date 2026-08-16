Num=int(input("Enter Number : "))
temp=1
sum=0
while(temp<=Num):
    if Num % temp ==0:
        sum+=temp
    temp+=1
print(sum)