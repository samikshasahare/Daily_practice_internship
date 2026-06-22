#1
dict1 = {'name':'ajay', 'age':20, 'city':'mumbai' }
print(dict1)
print(type(dict1))
#2
print(dict1['name'])
#3
dict1['email']='amit@gamil.com'#add
print(dict1)
#4
dict1['age']=21#update
print(dict1)
#5
my_dict = {"a": 1, "b": 2, "c": 3}
del my_dict["b"]
print(my_dict)
#6
print(len(dict1))
#7
my_dict = {"a": 1, "b": 2, "c": 3}
del my_dict["b"]
print(my_dict)
#8
print(dict1.keys())
#9
print(dict1.values())
#10
for key, value in my_dict.items():
    print(key, value)
#11
numbers = [1, 2, 3, 2, 1, 2, 4, 3, 1]
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)
#12
marks = {"Alice": 85,"Bob": 92,"Charlie": 78,"David": 95,"Eve": 88}
print(min(marks))
print(max(marks))
#13
total = sum(marks.values())
print(total)
#14
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)
#15
numbers = [1, 2, 3, 4, 5]
squares = {n: n**2 for n in numbers}
print(squares)
#16
for key, value in my_dict.items():
    print(key, value)
#17
numbers = {"hii":"H","yt":"Y"}
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)
#18
emp = {"name":"samm",3:{1:"python" , 2:"java"}}
print(emp)
#19
numbers = {"1st":"Hello","2nd":"Yuppp","3st":"Hello"}
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)
#20
inventory = {}
def add_item(name, quantity, price):
    if name in inventory:
        inventory[name]['quantity'] += quantity
    else:
        inventory[name] = {'quantity': quantity, 'price': price}
    print(f"{name} added/updated successfully.")
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
    else:
        print("\nCurrent Inventory:")
        for item, details in inventory.items():
            print(f"{item} - Quantity: {details['quantity']}, Price: {details['price']}")
def update_item(name, quantity):
    if name in inventory:
        inventory[name]['quantity'] = quantity
        print(f"{name} updated successfully.")
    else:
        print("Item not found.")
def delete_item(name):
    if name in inventory:
        del inventory[name]
        print(f"{name} deleted successfully.")
    else:
        print("Item not found.")
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update Item")
    print("4. Delete Item")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        add_item(name, qty, price)
    elif choice == '2':
        view_inventory()
    elif choice == '3':
        name = input("Enter item name: ")
        qty = int(input("Enter new quantity: "))
        update_item(name, qty)
    elif choice == '4':
        name = input("Enter item name to delete: ")
        delete_item(name)
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
#21