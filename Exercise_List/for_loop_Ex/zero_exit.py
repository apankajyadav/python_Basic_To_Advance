sum=0
for i in range(100):
    num=int(input("Enter Number : "))

    if num==0:
        break
    sum=sum + num
    i+=1  

print(f"sum of Enter Number is {sum}")
  