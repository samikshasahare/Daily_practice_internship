"""a=56
b=34
print("1.add \n2.sub \n3.mul \n4.div")
choice = int(input("enter your choice"))
if choice == 1:
    print("addition =",a+b)
elif choice == 2:
    print("substraction =",a-b)
elif choice == 3:
    print("multiplication =",a*b)
elif choice == 4:
    print("division =",a//b)
else:
    ("inalid choice")
#loop
s = "sumago"
for char in s:
    print(char)
#list tuple set
l1 = [1, 3, 5, 7, 8, 9]
for i in l1:
    print(i)
#dictiony
data = {'Name':"samm",'Addre':"bramhapuri"}
for k,v in data.items():
    print(f"{k}==>{v}")
#range()
for i in range(2,21,2):
    print(i)
for j in range(1,11,2):
    print(j)
#nested for loop
row =7
for i in range(1,row):
    for j in range(1,i):
        print("*",end=" ")
    print(" ")

for i in range(1,7):
    for j in range(1,i):
        print("*",end=" ")
    print(" ")

count = 0
while count < 10:
    print("Samm")
    count += 1

#infinite
while True:
    print("samiiii")
#loop contoral statement
# break, countinu, pass
for i in range(10):
    if i == 5:
        break
    print(i)
for i in range(10):
    if i == 5:
        continue
    print(i)
for i in range(10):
    if i == 5:
        pass
    print(i)

#practice session
#1
i=2
while i<=10:
    print(i)
    i+=2
#2
i=2
while i<=50:
    print(i)
    i+=2

#3
i=1
while i<=50:
    print(i)
    i+=2
#4
i=1
sum=0
while i<= 10:
    sum=sum+i
    i+=1
print("sum",sum)
#5
num = int(input("entera number"))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i+=1
#6
n=int(input("enetr number"))
count = 0
while n>0:
    n = n//10
    count +=1
print("Number of digit",count)
#7
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reverse =", reverse)
#8
num = int(input("Enter a number: "))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i += 1
print("Factorial =", fact)
# intermidate level
#1
i =0
while i<=10:
    if i==6:
        break
    print(i)
    i+=1
#2
i =0
while i<=10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1
#3
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
#4
numbers = [10, 20, 30, 40, 50]
search = int(input("Enter number to search: "))
i = 0
while i < len(numbers):
    if numbers[i] == search:
        print("Number found")
        break
    i += 1
else:
    print("Number not found")
#5
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    print("You entered:", num)
#6
i= 1
while i <= 10:
    if i % 3 == 0:
        pass
    else:
        print(i)
    i += 1
#7
password = ""
while password != "python":
    password = input("Enter password: ")
print("Correct password")
#8
count = 0
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    count += 1
print("Total numbers entered:", count)
#9
balance = 5000
while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        print("Balance =", balance)
    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        balance -= amount
        print("Remaining balance =", balance)
    elif choice == 3:
        print("Thank you")
        break
    else:
        print("Invalid choice")"""
#10
i = 1
while i <= 10:
    if i == 3:
        pass
    if i == 5:
        i += 1
        continue
    if i == 8:
        break
    print(i)
    i += 1


#2 loop practice 
n=int(input("Enter number: "))
i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1
#4
n = int(input("Enter N: "))
count = 0
i = 1
while i <= n:
    if i % 2 == 0:
        count += 1
    i += 1
print(count)
#5
n = int(input("Enter N: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i += 1
print(fact)
#6
n = int(input("Enter N: "))
while n >= 1:
    print(n, end=" ")
    n -= 1
#7
string = input("Enter string: ")
count = 0
i = 0
while i < len(string):
    if string[i].lower() in "aeiou":
        count += 1
    i += 1
print(count)
#8
n = int(input("Enter N: "))
i = 1
while i <= n:
    print("* " * i)
    i += 1
#9
n = int(input("Enter number of elements: "))
largest = None
i = 0
while i < n:
    num = int(input("Enter number: "))

    if largest is None or num > largest:
        largest = num
    i += 1
print(largest)
#10
n = int(input("Enter N: "))
i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
    i += 1