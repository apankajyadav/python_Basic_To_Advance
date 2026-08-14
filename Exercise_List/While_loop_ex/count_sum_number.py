# count and print the total number of digit in a given number !

Number=int(input("Enter Numnber : "))
count=0
if Number == 0:
    count+=1
else:
    count=0
    while(Number>0):
        Number=Number // 10
        count+=1
    print(count)