s_num=int(input("Entere starting range of number :"))
l_num=int(input("Entere ending range of number : "))

while(s_num<=l_num):
    if s_num%2==0:
        print(f"Number is Even {s_num}")
    s_num+=1