Num=int(input("Enter Number You want to chk : "))
temp=1
reslt=0
while(temp<Num):
    if Num % temp== 0:
        reslt+=temp
    temp+=1
    
if reslt == Num:
    print("Perfect Number ")
else:
    print("Not Perfect Number")