#Exercise 5
#Final Salary Calculater 

Basic_sal=int(input("Entere Basic Salary:"))
Bonus_amt= int(input("Entere Bonus :"))
Total_sal=Basic_sal+Bonus_amt

Tax_percent = int(input("Enter Tax in percent:"))
Tax_amt=Total_sal*Tax_percent/100

final_salary=Total_sal-Tax_amt
print(f"Tax Amount : {Tax_amt}")
print(f"Fianl Salary :{final_salary}")