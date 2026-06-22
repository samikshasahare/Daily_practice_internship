"""#practice session

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)  
        self.roll_no = roll_no

    def display_student(self):
        self.display()  
        print(f"Roll No: {self.roll_no}")
s = Student("Samm", 20, 101)
s.display_student()


#2
class vehical:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print(f"{self.brand} vehicle is starting...")

class car(vehical):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model = model
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")

car1 = car("Toyota", "Camry")
car1.start()
car1.display() 


#3
class employee:
    def __init__(self,emp_id):
        self.emp_id=emp_id
    def display(self):
        print(f"Name: {self.emp_id}")
class manager(employee):
    def __init__(self,emp_id,name):
        super().__init__(emp_id)
        self.name=name
    def show(self):
        print(f"emp_id: {self.emp_id}")
        print(f"name: {self.name}")
mag = manager(101,"samm")
mag.display()
mag.show()

#4
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Animals make sounds")
class Dog(Animal):
    def sound(self): 
        print(f"{self.name} says Woof!")
dog1 = Dog("sheruu")
print("Name:", dog1.name) 
dog1.sound()

#5
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ₹{amount}")
    def show_balance(self):
        print(f"Balance: ₹{self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest added: ₹{interest}")
acc = SavingsAccount("Samiksha", 100000, 5)
acc.show_balance()
acc.add_interest()
acc.show_balance()

#encapsulation
class Student:
    def __init__(self, name, marks):
        self.__name = name  
        self.__marks = marks    
    def display_record(self):
        print("Name:", self.__name)
        print("Marks:", self.__marks)
    def set_marks(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
student1 = Student("Amit", 85)
student1.display_record()
student1.set_marks(90)
student1.display_record()

#7
class Employee:
    def __init__(self,emp_id):
        self.__emp_id = emp_id
    def display_record(self):
        print("Employee id:", self.__emp_id)
    def get_id(self):
        return self.__emp_id
emp = Employee(1099)
emp.display_record()

#8 
class MobilePhone:
    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price  
    # Getter method
    def get_price(self):
        return self.__price
    # Setter method
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Invalid price!")
phone = MobilePhone("Samsung", 25000)
print("Price:", phone.get_price())
phone.set_price(30000)
print("Updated Price:", phone.get_price())


#10
class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin 
        self.__balance = balance  

    def check_balance(self, pin):
        if pin == self.__pin:
            print("Balance:", self.__balance)
        else:
            print("Incorrect PIN")

    def deposit(self, pin, amount):
        if pin == self.__pin:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Incorrect PIN")

    def withdraw(self, pin, amount):
        if pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawn:", amount)
            else:
                print("Insufficient Balance")
        else:
            print("Incorrect PIN")
atm = ATM(1234, 10000)
atm.check_balance(1234)
atm.deposit(1234, 2000)
atm.withdraw(1234, 3000)
atm.check_balance(1234)
"""
#polymophism


#Therotical session
#Exception Handling
#try except finally
#two types of Exception Built in and usr define

#type error"""
"""try:
    a=10
    b="sumago"
    c=a+b
except TypeError:
    print("do not add int and string")
#print(c)

#name error
try:
    print("value of x",x)
except NameError:
    print("variable is not define")

#zero division error
try:
    a=int(input("enter first num"))
    b=int(input("enter second num"))
    c=a/b
except ZeroDivisionError:
    print("do not divion by zero")
except ValueError:
    print("do not enter symbol,charcter")
else:
    print("division os ",c)
finally:
    print("always exceut")"""

""" #index error
try:
    l=[1,3,2,4,5]
    print(l[5])
except IndexError:
    print("index not found") """

""" 
#key error
try:
    data = {"name": "samm", "age": 18}
    print(data[1])

except KeyError:
    print("Key not found in dict") """