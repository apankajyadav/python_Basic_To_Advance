#sum of digit of even and odd"
sum_e=0
sum_o=0
for _ in iter(int,1):
    n=int(input("Enter Number :"))
    print("Enter Zero for Exit....")
    if n==0:
        break
    elif n % 2==0:
        sum_e=sum_e+n
    else:
        sum_o=sum_o+n
print(f"sum of Even Digit {sum_e}")
print(f"sum of Odd Digit {sum_o}")