#check armstrong or not 
num=1535
temp=num
res=0

for i in range(len(str(num))):
    digit=temp % 10   
    res=res + digit**len(str(num))
    temp=temp // 10
if res==num:
    print("Number is Armstrong")
else:
    print("Number Not Armstrong")