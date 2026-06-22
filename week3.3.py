#function
"""defualt function()
def student(name,age=17):
    print(f"name is {name}")
    print(f"age is {age}")
student("samm")
student("samm",18)


#variable leng
def number(*args):
    for i in args:
        print(i)
number(1,2,3,4,5,6)
number(1,2,"pineapple","coconut",345,True)


def Information(name,*args):
    print("Name is",name)
    for i in args:
        print(i)
Information("samm",17,18)

def sum_n(*args):
    return sum(args)
add=sum_n(1,3,4)
print(add)

def addition(*args):
    total=0
    for n in args:
        total+=n
    print("total is ",total)
addition(2,4,5,2,8,8)



#kwargs(keyword variable len argument)
def student(name,**kwargs):
    print("name is",name)
    for k,v in kwargs.items():
        print(f"{k}==>{v}")
student(name="samm",sub1=90,sub2=92,sub3=98)"""

#lambda function(anoymous fun)fuction without name
#syntax
#lambda arguments : expression
"""add = lambda x,y:x+y
print(add(20,48))
max_n = lambda a,b:max(a,b)
print(max_n(28,90))
max_n = lambda a,b:a if a>b else b
print(max_n(20,70))

a = int(input("enter num   "))
no_is = lambda a:"even" if a%2==0 else "odd"
print(no_is(a))

#filter and map
list1[1,4,-4,9,8]
pos =[]
neg =[]
for i in list1:
    if i>0:
        pos.append(i)
    else
        neg.append(i)
print(pos)
print(neg)

#filter
#synax
#filter(function:  ,   )
l1=[1,4,9,8,8,3,2,1]
even=lambda x: x%2==0
even_list=(filter(even,l1))
print(even_list)

#map function
l1=[1,4,9,8,8,3,2,1]
sqr=lambda a:a**2
sqr_list=list(map(sqr,l1))
print(sqr_list)

#reduce function
#returns single value
from functools import reduce
l1=[1,4,9,8,8,3,2,1]
nums = [1, 2, 3, 4]
add = lambda x,y:x+y
total=reduce(add,l1)
print(total)

#practice sestion
def squre(n):
    return(n*n)
num=squre(4)
print(num)


def cube(a):
    return(a*a*a)
num=cube(4)
print(num)


def addd(x):
    return(x+x)
num=addd(4)
print(num)


def product(y):
    return(y*y)
num=product(4)
print(num)


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
num = factorial(4)
print(num)

def rev_str(s):
    return s[::-1]
result = rev_str("hello")
print(result)

def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count
num = count_vowels("Hello World")
print(num)

def largest_char(text):
    return max(text)
result = largest_char("hello")
print(result)

def largest_char(text):
    return min(text)
result = largest_char("hello")
print(result)

def average(a, b, c, d, e):
    return (a + b + c + d + e) / 5
avg = average(10, 20, 30, 40, 50)
print(avg)

#basic function
def greet():
    print("Hello,World!")
greet()

def display_name():
    name = input("Enter your name: ")
    print(name)
display_name()

def number():
    for i in range(1, 11):
        print(i)
number()

def even_no():
    for i in range(1, 21):
        if i%2==0:
            print(i)
even_no()"""

def odd_no():
    for i in range(1, 21):
        if i%2!=0:
            print(i)
odd_no()

def table_():
    for i in range(1, 50):
        if i%5==0:
            print(i)
table_()

def squre(n):
    print("squre ",n*n)
squre(4)

def cube(n):
    print("cube ",n*n*n)
cube(4)

def summ(n , m):
    print("sum",n + m)
summ(4,7)

def pro(n , m):
    print("multiplication",n * m)
pro(4,7)

def div(n , m):
    print("division",n // m)
div(16,8)

def maximum(a, b):
    if a > b:
        return a
    else:
        return b
result = maximum(10, 20)
print(result)

def manimum(a, b):
    if a < b:
        return a
    else:
        return b

result = manimum(10, 20)
print(result)

def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_odd(9)

def positive_negative(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
positive_negative(-6)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5)) 

def divide_by_5(n):
    if n % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible by 5"
print(divide_by_5(25))

def count_characters(s):
    return len(s)
print(count_characters("hello")) 

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(largest_of_three(10, 25, 15)) 

#lambda Function
sq = lambda x:x*x
print(sq(2))

cube = lambda x:x*x*x
print(cube(2))

add = lambda x,y:x+y
print(add(2,8))

mul = lambda x,y:x*y
print(mul(2,8))

div = lambda x,y:x/y
print(div(16,8))

maxx = lambda a,b:a if a>b else b
print(maxx(3,9))

minn = lambda a,b:a if a<b else b
print(maxx(3,9))

check_num = lambda a:"even" if a%2==0 else "odd"
print(check_num(3))

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(celsius_to_fahrenheit(0))

def divide_by_3(n):
    if n % 3 == 0:
        return "Divisible by 3"
    else:
        return "Not divisible by 3"
print(divide_by_3(25))

def area_rectangle(length, width):
    return length * width
print(area_rectangle(10, 5))

def perimeter_rectangle(length, width):
    return 2 * (length + width)
print(perimeter_rectangle(10, 5))

def simple_interest(p, r, t):
    return (p * r * t) / 100
print(simple_interest(1000, 5, 2)) 

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(celsius_to_fahrenheit(25))  

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
print(fahrenheit_to_celsius(77)) 


#filter
#1
abc=[10,15,22,33,40,55,60]
print(abc)
even=list(filter(lambda a: a%2==0 ,abc))
print("even numbers=",even)
#2
a=[-10,5,-3,8,0,15,-7]
print(a)
p=list(filter(lambda s: s>0 ,a))
print(p) 
#3
lst=["Aman","Rahul","Anjali","Priya","Akash"]
a=(list(filter(lambda z: z.startswith("A") ,lst)))
print(a)
#4
lst=["cat","elephent","dog","tiger","hippotamus"]
long=list(filter(lambda l: len(l)>5 ,lst))
print(long)
#5
salary={"sagar":50000, "bharat":60000, "guddu":4000, "shruti":30000,"shreya":100000}
s=list(filter(lambda x: x[1]>40000 , salary.items()))
print(s) 


#map task
#1
square=[1,2,3,4,5]
s=list(map(lambda x: x*x ,square))
print(s)

#2
lst=["rahul","aman","priya","neha"]
a=list(map(lambda z: z.upper(),lst))
print(a)
#3
a=[0,20,30,40]
c=list(map(lambda s:(s*9/5)+32,a))
print(c) 
#4
g=[100,200,300,400]
abc=list(map(lambda x:(x*18/100+x),g))
print(abc)
#5
salary=[30000,40000,50000]
increase=list(map(lambda x:x+(x*10/100),salary))
print(increase)


#reduce 
#1
from functools import reduce 
a=[10,20,30,40,50]
sum=reduce(lambda x,y:x+y,a)
print(sum)

#2
from functools import reduce
a=[25,80,15,100,45]
maxium=reduce(lambda x,y: x if x>y else y,a)
print("maxium number:-",maxium)

#3
from functools import reduce
a=[1,2,3,4,5]
multiplication=reduce(lambda x,y:x*y,a)
print("multiplication=",multiplication) 

 #4
from functools import reduce
string=["python","is","awesome"]
concat=reduce(lambda x,y: x+y,string)
print("concatinate string:-",concat)

 #5
from functools import reduce
salary={"sagar":50000, "bharat":60000, "guddu":4000, "shruti":30000,"shreya":100000}
total=reduce(lambda x,y: x+y,salary.values())
print(total) 

