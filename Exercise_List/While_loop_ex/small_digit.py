
Number=7058183215
greater=0
while Number>0:
        digit=Number % 10
        if digit>greater:
            greater=digit
        Number=Number // 10
print(greater)


