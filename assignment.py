#part1
#1
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=a+b
print("The sum of the two numbers is:", c)

#2 area of ractangle
length=float(input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))    
area=length*width
print("The area of the rectangle is:", area)

#3squre and cube of a number
num=int(input("Enter a number: "))
square=num**2
cube=num**3
print("The square of the number is:", square)
print("The cube of the number is:", cube)

#4 find quotient and remainder
dividend=int(input("Enter the dividend: "))
divisor=int(input("Enter the divisor: "))
quotient=dividend//divisor
remainder=dividend%divisor
print("The quotient is:", quotient)
print("The remainder is:", remainder)

#5 convert total min into hours and min
total_minutes=int(input("Enter total minutes: "))
hours=total_minutes//60
minutes=total_minutes%60
print("The time is:", hours, "hours and", minutes, "minutes")


#part 2
#6 check two no. are equal or not
num1 =int(input("Enter the first number: "))
num2 =int(input("Enter the second number: "))
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

#7
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
if x > y:
    print("first number is greater than the second number.")
elif x < y:
    print("second number is greater than the first number.")
else:
    print("Both numbers are equal.")

#8 greter among three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print(" greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print(" greatest number is:", num2)
else:
    print("greatest number is:", num3)

#9
marks =int(input("Enter a number: "))
if marks >= 40:
    print("pass")
else:
    print("fail")

#10
age = int(input("Enter your age: "))
if age >= 18:
    print("eligible to vote.")  
else:
    print("not eligible to vote.")

#11 ASIGNMENT OPERATORS
a = 10  
a += 5  
print(a)  
a -= 3  
print(a)   
a *= 2  
print(a)  
a /= 4 
print(a) 

#12 
balance = 1000
withdrawal = int(input("Enter the amount to withdraw: "))
if withdrawal <= balance:
    balance -= withdrawal
    print("Withdrawal successful. Remaining balance:", balance)
else:
    print("Insufficient balance. Withdrawal failed.")

#13
CGPA = float(input("Enter your CGPA: "))
backlog = int(input("Enter the number of backlogs: "))
if CGPA >= 7.0 and backlog == 0:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")

#14 age or membership fee eligibilityfor a club
age = int(input("Enter your age: "))
membership_fee = float(input("Enter the membership fee: "))
if age >= 18 and membership_fee >= 100:
    print("You are eligible for the club membership.")
else:
    print("You are not eligible for the club membership.")

#16 check character in a string
string = input("Enter a string: ")
character = input("Enter a character to check: ")
if character in string:
    print(f"The character '{character}' is present in the string.")
else:
    print(f"The character '{character}' is not present in the string.") 

#17 check students name in a list
students = ["Alice", "Bob", "Charlie", "David"]
name = input("Enter a student's name: ")
if name in students:
    print(f"{name} is a student in the list.")
else:
    print(f"{name} is not a student in the list.")

#18 check no. in tuple
numbers = (1, 2, 3, 4, 5)
num = int(input("Enter a number to check: "))
if num in numbers:
    print("The number is present in the tuple.", num)
else:
    print("The number is not present in the tuple.", num)

#19 check variable refers to the same object
a = [1, 2, 3]
b = a
if a is b:
    print("a and b refer to the same object.")
else:
    print("a and b do not refer to the same object.")

#20 comparison  two list using == and is operator
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if list1 == list2:
    print("list1 and list2 are equal using == operator.")
else:
    print("list1 and list2 are not equal using == operator.")
if list1 is list2:
    print("list1 and list2 refer to the same object using is operator.")
else:
    print("list1 and list2 do not refer to the same object using is operator.")


#21 find largest and smallest no among three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)
#or
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
print("The largest number is:", largest)
print("The smallest number is:", smallest)

#22 simmle calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
    print("The result is:", result)
elif operator == "-":
    result = num1 - num2
    print("The result is:", result)
elif operator == "*":
    result = num1 * num2
    print("The result is:", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")

#23 check leaf year
year = int(input("enter a year: "))
if (year % 4 ==0 and year% 100 !=0) or (year % 400 ==0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#24 check div by 3 and 5 or both
num = int(input("Enter a number: "))
if num%3 ==0 and num%5 ==0:
    print(num, "is divisible by both 3 and 5.")
elif num%3 ==0:
    print(num, "is divisible by 3.")
elif num%5 ==0:
    print(num, "is divisible by 5.")
else:
    print(num, "is not divisible by 3 or 5.")

#C.2
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
