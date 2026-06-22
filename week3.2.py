#function
"""positional
keyword
default 
variable len
def student():
    name="samm"
    age=18
    print(f"name is {name}")
    print(f"age is {age}")

student()#function call
4
#parametrized fun
def student(name,age):
    print(f"name is {name}")
    print(f"age is {age}")
student("sammm",18)
#positional
student(18,"sammm")
#keyword argu
student(age=18,name="sammm")"""


#python funtion Excersice
#basic level
"""def add_number(a,b):
    print(a+b)
add_number(1,2)
def is_even(num):
    if num%2==0:
        print("true")
is_even(4)
def find_square(n):
    print(n*n)
find_square(4)
def greet(name):
    print("Hello",name)
greet("samm")
def max_of_two(a,b):
    print(max(a,b))
max_of_two(2,9)

#intermediate level
def factorial(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i += 1
    print(fact)
factorial(5)
def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count
print(count_vowels("sammii"))
def revers_string(s):
    return s[::-1]
print(revers_string("hello"))
def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(check_prime(7))   
print(check_prime(10))
def sum_list(lst):
    return sum(lst)
print(sum_list([1,2,3,4]))
def find_max(lis):
    return max(lis)
print(find_max([3,7,3,8,9,2]))
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
def word_count(s):
    return len(s.split())
print(word_count("Hello world Python"))
def palindrome(s):
    s = str(s)
    return s == s[::-1]
print(palindrome("madam"))
print(palindrome("hello"))   
print(palindrome(121))
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operator"
print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*')) 
print(calculator(10, 5, '/'))
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result
print(fibonacci(10))
def char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq
print(char_frequency("hello"))
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d) ** power for d in digits)
    return total == n
print(is_armstrong(153)) 
print(is_armstrong(123))   
#def sort_dict_by_value(d):
#   return dict(sorted(d.items(), key=lambda item: item[1])
#d = {"a": 3, "b": 1, "c": 2}
def password_strength(p):
    if len(p) < 6:
        return "Weak"
    elif len(p) < 10:
        return "Medium"
    else:
        return "Strong"
print(password_strength("abc2346ji"))
def decimal_to_binary(n):
    return bin(n)[2:]
print(decimal_to_binary(10))"""