a=2
b=4
hcf=1
for i in range(1, min(a,b)+1):
    if a % i== 0  and b % i==0:
        hcf=i
print(hcf)