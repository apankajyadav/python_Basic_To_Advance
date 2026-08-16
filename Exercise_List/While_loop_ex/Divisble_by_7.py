#find Divisible by 7
a=int(input("Enter Start Number " ))
b=int(input("Enter end Number " ))

while(a<=b):
    if a % 7==0:
        print(f"{a} is Divisible By 7")
    a+=1