#set 1
#1
num =int(input("enter a digit"))
if num>0:
    print("digit is positive")
else:
    print("digit is negative")
#2
num =int(input("enter a digit"))
if num%2:
    print("digit is even")
else:
    print("digit is odd")
#3
age =int(input("enter a persons age:"))
if age >= 18:
    print("person is eligible for vote")
else:
    print("person isn't eligible for vote")
#4
num =int(input("enter a digit"))
if num%5:
    print("digit is divisible by 5")
else:
    print("digit isn't divisible by 5")
#5
num1 =int(input("enter a first digit"))
num2 =int(input("enter a second digit"))
if num1>num2:
    print("first digit is greater than second digit")
else:
    print("second digit is greater than first digit") 
#6
num =int(input("enter a digit"))
if num==0:
    print("digit is zero")
else:
    print("digit isn't zero")
#7
year =int(input("enter your year:"))
if year%4:
    print("year is leap year")
else:
    print("year isn't leap year")
#8
alpha =('a','e','o','u','i','A','E','O','U','I')
alphabet =int(input("enter your alphabet:"))
if alphabet==alpha:
    print("Alphabet is vowel")
else:
    print("Alphabet is consonant")
#9
num =int(input("enter a digit"))
if num%2&3:
    print("digit is divisible by 2&3")
else:
    print("digit isn't divisible by 2&3")
#10
num =int(input("enter a digit"))
if num*10:
    print("digit is multiple by 10")
else:
    print("digit isn't multiple by 10")


#set 2
#1
num= float(input("Enter a number: "))
if num > 0:
    print("Positive (+ve)")
elif num < 0:
    print("Negative (-ve)")
else:
    print("Zero")
#2
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("Largest number is:", largest)
#3
marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
#4
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)
elif units <= 300:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)
else:
    bill = (100 * 1.5) + (100 * 2.5) + (100 * 4) + ((units - 300) * 6)
print("Electricity Bill = ₹", bill)

#5
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Symbol")
#6
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("It is a Triangle")
else:
    print("It is NOT a Triangle")
#7
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a Triangle")
#8
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2 only")
elif num % 3 == 0:
    print("Divisible by 3 only")
else:
    print("Divisible by neither 2 nor 3")

#9
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))
if years > 5:
    bonus = salary * 0.05
    print("Bonus =", bonus)
    print("Total Salary =", salary + bonus)
else:
    print("No Bonus")
    print("Total Salary =", salary)
#10
price = int(input("enter a price"))
sell_price= int(input("enter a selling price"))
if price<sell_price:
    print("profit")
else:
    print("loss")