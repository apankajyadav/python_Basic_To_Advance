#check enter number is Armstone or not !
Num=int(input("Enter Number You want to chechk its amrngstone or not : "))
result=0
temp=Num
digits=len(str(Num))

while( temp > 0):
    digit=temp % 10 
    result=result + (digit **digits)
    temp = temp // 10

if Num == result:
    print(" Number is Amrngstone")
else:
    print("Non Amangstrone")

