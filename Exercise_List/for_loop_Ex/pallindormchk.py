Num=12157498
temp=Num
rev=0
for i in range(len(str(Num))):
    digit=temp % 10
    rev=rev * 10 + digit
    print(rev)
    temp=temp // 10 
if Num==rev:
    print("pallindrom")
else:
    print("Not pallindrom")
