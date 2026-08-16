num=int(input("Enter Number You want to find Factors : "))
temp=1
factors=" "

while(num>=temp):
    if num % temp == 0:
        factors+=str(temp) +" , "
        
    temp+=1
print(f"Factors of {num} are {factors[:-2]}")