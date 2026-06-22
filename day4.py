#string
name = '  python tutorial  '
print("Name is ",name)
text = """hellooo it's me 
sammmmmm"""
print(text)

print(name[2])
print(name[-2])
print(name[2:5])
print(name[2:6])
print(name[2::6])
print(name[::2])
print(name[::-1])

#function string
print(len(name))
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())
print(name.count('o'))
print(name.index('o'))
print(name.strip())
print(name.rstrip())
print(name.lstrip())
s=name.replace('python','java')
print(s)
print(name.isalpha())
print(name.islower())
print(name.isdigit())
print(name.startswith (' '))
print(name.startswith ('y'))

#listt
car=['bmw','toyota','thar','audii']
#print(car,type(car))
print(car[3])
print(car[1:4])
list2=[['python','django'],['java','spring']]
print(list2[1][1])

#split method (for taking multipal input)
#name,address = input("enter nam and add").split()
#print(name,"nameee")
#print(address,"address")

car=['bmw','toyota','thar','audii']
car.append("alto")
print(car)
list1=['apple','cherry']
car.extend(list1)
print(car)
list1.insert(2,"kiwi")
print(list1)
car.remove('alto')
print(car)
car.pop()
print(car)
print(len(car))
car.sort()
print(car)
car.reverse()
print(car)
car1=car.copy()
print(car1)
car1.clear()
print(car1)