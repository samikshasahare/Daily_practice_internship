#1
book_name = input("Enter Book Name: ")
available_copies = int(input("Enter Available Copies: "))

if available_copies > 5:
    print("Book Issued Successfully")
else:
    print("Book Not Available")
#2
late_days = int(input("Enter Late Days: "))
fine_amount = late_days * 10
print("Fine Amount =", fine_amount)
#3
name = input("enter your name")
membership_status = input("enter membership status")
if membership_status == "Active" :
    print ("book borrowing allowed")
#4
borrowed_books = int(input("Enter Borrowed Books (no): "))
max_limit = 5
if borrowed_books < max_limit:
    print("You Can Borrow More Books")
else:
    print("Maximum Book Limit Reached")
#mini project
membership = input("Enter Membership Status: ")
available_copies = int(input("Enter Available Copies: "))
borrowed_books = int(input("Enter Borrowed Books: "))
max_limit = 3
if membership == "Active" and available_copies > 0 and borrowed_books < max_limit:
    print("Book Issued Successfully")
else:
    print("Book Issue Failed")
#practice question
#1
book_name = input("enter book name")
copies = int(input("Enter available copies: "))
if copies > 0:
    print("Book Available")
else:
    print("Book Not Available")
#2
late_days = int(input("Enter late days: "))
fine = late_days * 10
print("Fine Amount =", fine)
#3
status = input("Enter membership status: ")
if status == "Active":
    print("Membership Verified")
else:
    print("Membership Not Valid")
#4
books = int(input("Enter borrowed books: "))
if books < 5:
    print("You Can Borrow More Books")
else:
    print("Borrowing Limit Reached")
#5
membership = input("Enter membership status: ")
copies = int(input("Enter available copies: "))
books = int(input("Enter borrowed books: "))
if membership == "Active" and copies > 0 and books < 5:
    print("Book Issued Successfully")
else:
    print("Book Issue Failed")
#6
reserved_book = input("is book is reserved (yes/no)")
if reserved_book =="no":
    print("book can be issued")
else:
    print("book reserved for Another student")
#7
fine = int(input("enter fine amount"))
membership = input("enter membership type")
if membership == "premimum":
    fine = fine - (fine*(20/100))
print("fine",fine) 
#8
fine = int(input("enter pending fine: "))
if fine > 100:
    print("borrowing restricted")
else:
    print("Borrowing allowed")
#9
registered = input("Are you registered? (Yes/No): ")
if registered == "Yes":
    print("Digital Library Access Allowed")
else:
    print("Access Denied")
#10
issue = input("Enter issue status (Success/Fail): ")
if issue == "Success":
    print("Book Issue Request Successful")
else:
    print("Book Issue Request Failed")