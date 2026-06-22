t1 = (10, 3, 5, 35, 5, 45)
print(t1)
print(type(t1))
#2
print(t1[0])
print(t1[-1])
#3
print("0ccurance of element",t1.count(5))
#4
print(len(t1))
#5
l1 = list(t1)
print(l1)
print(type(l1))
l1.append(56)
print(l1)
#6
print("maximum",max(t1))
print("minimum",min(t1))
#7
print(sum(t1))
#8
num = 20
if num in t1:
    print("element exixts")
else:
    print("does not")
#9
t=("samm",18,"computer")
name, age, branch =t
print("name",name)
print("age",age)
print("branch",branch)
#10
tu1 = (" samm, 10,(10, 34, 4), 478")
print(tu1)    