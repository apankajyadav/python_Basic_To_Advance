Num=758183215
S_digit= Num % 10
Num=Num // 10 
while (Num>0):
    digit=Num % 10
    if S_digit>digit:
        S_digit=digit
    Num=Num // 10
print(S_digit)

