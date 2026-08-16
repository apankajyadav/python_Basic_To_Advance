# Find Largests number among user input .exit when usere enter 0.
user_input=[]
largest=0
for i in range(1,101):
    num=int(input("Enter Number "))
    if num == 0:
        break
    else:
        user_input.append(num)
        if num>largest:
            largest=num
#print(user_input)
print(f"Largest Number Enter by user is {largest}")