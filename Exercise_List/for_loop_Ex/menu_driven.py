for i in range(5):
    print("List of Menu")
    print("1.ADDITION")
    print("2.MULTIPICATION")
    print("3.SUBSTRACTION")
    print("5.Exit")

    User_choice=int(input("Enter Your Choice from Menu: "))

    if User_choice==1:
        a=int(input("please Enter Number:"))
        b=int(input("Please Enter onother Number : "))
        resultadd=a+b
        print(f"sum of Number {resultadd}")

    if User_choice==2:
            a=int(input("please Enter Number:"))
            b=int(input("Please Enter Another Number : "))
            resultmul=a*b
            print(f"Multipication of Number {resultmul}")

    if User_choice==2:
                a=int(input("please Enter Number:"))
                b=int(input("Please Enter Another Number : "))
                resultmul=a*b
                print(f"Multipication of Number {resultmul}")

    if User_choice==3:
                    a=int(input("please Enter Number:"))
                    b=int(input("Please Enter Another Number : "))
                    resultmul=a-b
                    print(f"Multipication of Number {resultmul}")

    elif User_choice==5:
            print("Exiting....")
            break

    else:
            print("Invalid Input retry ...")