my_list = [10, 20, 30, 40, 50]
print(my_list[2])
print(len(my_list))
if not my_list:
    print("List is empty")
else:
    print("List is not empty")
#2
my_list = [1, 2, 3, 4, 5]
my_list[1] = 200
print(my_list)
my_list.append(600)
print(my_list)
my_list.insert(2, 300)
print(my_list)
my_list.remove(600)
print(my_list)
my_list.remove(my_list[0])
print(my_list)
#3
my_list = [10, 20, 30, 40, 50]
#calculate sum and average
total = sum(my_list)
average = total / len(my_list)
print("Sum:", total)
print("Average:", average)
#4
list1 = [2, 8, 15, 1, 9]
print("Smallest:", min(list1))
print("Largest:", max(list1))
#5
my_list = ['criket', 'football', 'tennis', 'hockey','football']
print(my_list.count('football'))
#6
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
combined_list = list1 + list2
print(combined_list)
#7
my_list = [10, 20, [5000, 6000], 30, 40]
my_list[2].append(7000)
print(my_list)
#8
num = [23, 34, 'hello', 32, 56]
print(len(num))
#9
num = [23, 34, 'hello', 32, 56]
print(num[::-1])
#10
list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    index = list1.index(20)
    list1[index] = 200
print(list1)