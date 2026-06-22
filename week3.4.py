#class
"""class Employee:
    #default counstructor
    def __init__(self):
        self.name="john"
        self.salary=30000
    def Display(self):
        print("employee name is",self.name)
        print("salary is",self.salary)
emp = Employee()
emp.Display()

class Student:
    def __init__(self):
        self.name="reva"
        self.age=18

    def display(self):
        print("student name is",self.name)
        print("age is",self.age)
emp = Student()
emp.display()

#parametrized constr

class Employee:
    #default counstructor
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        
    def Display(self):
        print("employee name is",self.name)
        print("salary is",self.salary)
emp = Employee("samm",300000)
emp.Display()

#inheritance
class Animal:
    def __init__(self):
        self.name=" "
    def show(self):
        print(f"animal namee is {self.name}")
class cat(Animal):
    def make_sound(self):
        return "cat sound is meow"
c=cat()
c.name="cat"
print(c.name)
print(c.make_sound())




#multiple inheritance
class Father:
    def __init__(self):
        self.fname="abc"
    def father(self):
        print(f"father name is {self.fname}")

class Mother:
    def __init__(self):
        self.mname="xyz"
    def mother(self):
        print(f"mother name is {self.mname}")

class child(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.cname="samm"
    def child(self):
        print(f"child name is {self.cname}")

c=child()
c.father()
c.mother()
c.child()


#multilevel 
class Grandfather:
    def __init__(self):
        self.gname="abc"
    def Grandfather(self):
        print(f"grandfather name is {self.gname}")
class Father:
    def __init__(self):
        Grandfather.__init__(self)
        self.fname="abc"
    def father(self):
        print(f"grandfather name is {self.fname}")

class Child(Father):
    def __init__(self):
        Father.__init__(self)
        self.cname="samm"
    def child(self):
        print(f"child name is {self.cname}")
obj=Child()
obj.Grandfather()
obj.father()
obj.child()"""


#Student Class
"""class Student:
    def __init__(self):
        self.name="reva"
        self.age=18

    def display(self):
        print("student name is",self.name)
        print("age is",self.age)
emp = Student()
emp.display()

#Employee class
class Employee:
    def __init__(self,name,salary,emp_id):
        self.name=name
        self.salary=salary
        self.emp_id=emp_id
    def Show_details(self):
        print("employee name is",self.name)
        print("salary is",self.salary)
        print("emp_id  is",self.emp_id)
emp = Employee("samm",300000,929)
emp.Show_details()

#car class
class car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display_car(self):
        print("car brand is",self.brand)
        print("model is ",self.model)
        print("price ",self.price)
obj = car("BMW","BMW 3series",4500000)
obj.display_car()

#book class
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_info(self):
        print("Book title is",self.title)
        print("Author is ",self.author)
        print("price ",self.price)
carr = Book("Harry Potter","J.K.Rowling",450)
carr.display_info()"""

#rectangle
class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def calculate_area(self):
        print("Length title is",self.lenght)
        print("Width is ",self.width)
rec = Rectangle(6,9)
rec.calculate_area()

#circle calss
class circle:
    def __init__(self,radius):
        self.radius=radius
    def calu_radius(self):
        print("radius",self.radius)
cir = circle(3.7)
cir.calu_radius()

#Bank Account 
class BankAccount:
    def __init__(self, acc_no, holder_name, balance):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Balance:", self.balance)
account = BankAccount(101, "Samiksha", 5000)
account.deposit(2000)
account.withdraw(1000)
account.check_balance()


#ptoduct Classss
class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
    def add_stock(self, qty):
        self.quantity += qty
    def remove_stock(self, qty):
        if qty <= self.quantity:
            self.quantity -= qty
        else:
            print("Stock not available")
    def display_product(self):
        print(self.product_id, self.name, self.quantity, self.price)
p = Product(1, "Laptop", 5, 50000)
p.add_stock(2)
p.remove_stock(1)
p.display_product()


#Mobilr classss
class Mobile:
    def __init__(self, brand, model, RAM, price):
        self.brand = brand
        self.model = model
        self.RAM = RAM
        self.price = price
    def display_specs(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("RAM:", self.RAM)
        print("Price:", self.price)
m = Mobile("Samsung", "Galaxy A55", "8GB", 40000)
m.display_specs()


#LibraryBook class
class LibraryBook:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies
    def issue_book(self):
        if self.copies > 0:
            self.copies -= 1
            print("Book issued")
        else:
            print("Book unavailable")
    def return_book(self):
        self.copies += 1
        print("Book returned")
    def display_details(self):
        print(self.book_id, self.title, self.author, self.copies)
b = LibraryBook(1, "Wings of Fire", "A.P.J Abdul Kalam", 3)
b.issue_book()
b.return_book()
b.display_details()