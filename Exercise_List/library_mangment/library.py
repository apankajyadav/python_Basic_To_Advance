books=[] #Avilable Books list
members=[] #Member List 
issued_books =[] #Issued Book list
def add_book():
    bookid=(input("Enter Book_id you want to Add:"))
    title=input("Enter Book Title:")
    author=input("Enter Book Author Name :")
    category=input("Enter Category:")
    quantity=int(input("Enter Quantity of Book:"))
    book={
        "id":bookid,
        "title":title,
        "author":author,
        "category":category,
        "quantity":quantity

    }
    books.append(book)
    print("Book Added Sucessfully")
def view_books():
    if len(books) == 0:
        print("No Books Avilable.")
        return
    print("\n==============================AVILABLE BOOKS ===============================================")

    for book in books:
        print("Book ID:",book["id"])
        print("Book Title:",book["title"])
        print("Book Author:",book["author"])
        print("Book Category:",book["category"])
        print("Book Quantity:",book["quantity"])
        print("-----------------------------------------------------------------------------------------")
def search_book():
    search=input("Enter Book Id,Title, or Author :").lower()

    found = False
    for book in books:
        if (search in book["id"] or search in book["title"].lower() or search in book["author"].lower()):
            print("\n Book Found")
            print("Book Id:",book["id"])
            print("Book Title:",book["title"])
            print("Book Author:",book["author"])
            print("Book Category:",book["category"])
            print("Book Quantity:",book["quantity"])

            found =True
    if not found:
        print("Book not Found.")

def register_member():
        m_id=(input("Enter User Id :"))
        name=(input("Enter User Name you want to Add:"))
        email=input("Enter Your Email :")
        phone=input("Enter Phone_Number:")
        
        member={
            "id":m_id,
            "name":name,
            "email":email,
            "phone":phone,
        }
        members.append(member)
        print("User Succesfully Register....!!")


def view_member():
    if len(members) == 0:
        print("No Member Registerd.")
        return
    print("\n==============================AVILABLE MEMBERS ===============================================")
    
    for member in members:
        print("Member Id:",member["id"])
        print("Member Name :",member["name"])
        print("Memebr Email:",member["email"])
        print("Memeber Phone Number:",member["phone"])
        print("-----------------------------------------------------------------------------------------")

def issue_book():
    member_id=input("Enter Member ID :")
    book_id=input("Enter Book ID :")

    #Find Member 
    member= None
    for m in members:
        print(m)
        if m["id"]==member_id:
            member = m
            break

    if member is None:
        print("Member Not Found.")
        return

    #Find Book
    book=None
    for b in books:
        if b["id"] == book_id:
            book=b
            break

    if book is None:
        print("Sorry!! Book Not found.")
        return


    #Check Avialibity
    if int(book["quantity"])<=0:
        print("Sorry!! This Book Currently Avilabe")
        return

    #issue Book
    book["quantity"]-=1

    #Issue_Record
    issue_record={
    "member_id":member_id,
    "book_id":book_id
    }
    issued_books.append(issue_record)   
    print("\n Book Issue Succesfully ")
    print("Member Name ",member["name"])
    print("Book Ttile ",book["title"])

def return_book():
    member_id=input("Enter Member ID :")
    book_id=input("Entere Book ID:")

    #Find issue Record
    issue_record=None

    for record in issued_books:
        if record ["member_id"] == member_id and record["book_id"]==book_id:
            issue_record = record
            break
    if issue_record is None:
        print("No issue Record Found.")
        return

    #Find The Book
    book = None

    for b in books:
        if b["id"] == book_id:
            book = b
            break

    if book is None:
        print("Book Not Found.")
        return
    #Increase Book  Quantity
    book["quantity"]+=1

    #Remove Issue Record
    issued_books.remove(issue_record)

    print("\n Book Returend Successfully!")
    print("Book:",book["title"])


print("-------------------------------------------------------------------------------------------------------------------------------------")

def view_issued_books():
    if len(issued_books) == 0:
        print("No Books are Currently issued.")
        return
    print("\n=================================================List Of Issued Book========================================================================")

    for record in issued_books:
        member= None
        book=None
        #Find Member Details 
        for b in members:
            if b["id"] ==record["member_id"]:
                book=b
                break
            print("Member Id:",record["member_id"])
            print("Member Name:",record["name"])
            print("BOOK Name:",book["title"])
            print("----------------------------------------------------------------------------------------------------------------------------")


def main_menu():

    while True:

        print("\n========== LIBRARY MANAGEMENT SYSTEM ==========")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Register Member")
        print("5. View All Members")
        print("6. Issue Book")
        print("7. Return Book")
        print("8. View Issued Books")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            register_member()

        elif choice == "5":
            view_member()

        elif choice == "6":
            issue_book()

        elif choice == "7":
            return_book()

        elif choice == "8":
            view_issued_books()

        elif choice == "9":
            print("Thank you for using Library Management System!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 9.")



main_menu()



