num=2
end=100
print("1 is not prime Number ")
while(num<=end):
    i = 2
    is_prime= True
    while i < num:
        if num % i ==0:
            is_prime= False
            break
        i+=1
    if is_prime:
        print(num)
    num+=1