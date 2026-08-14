Num=int(input("Enter Number you want to check : "))
i=2
is_prime= True 
    
while i < Num:
    if Num % i ==0:
        is_prime = False
        break
    i+=1
  
if is_prime and Num >1:
  print("Number is prime")
else:
  print("Not Prime Number")
  
    