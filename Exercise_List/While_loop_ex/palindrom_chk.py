Num=int(input(" Enter Number you want to check Palindrom :"))
copy_num=Num
Rev=0
while(Num>0):
    digit=Num % 10
    Rev=Rev * 10 + digit
    Num=Num // 10
if copy_num == Rev:
    print("Enter Number is Palindroom")
else:
    print("Enter number is not pallindorom")

    