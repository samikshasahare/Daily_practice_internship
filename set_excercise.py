s1 = {"Appple","mango","banana","coconut","pineapple"}
print(s1)
#2
s2 = {"red","white","green","black","white"}
print(len(s2))
#3
s3 = {10, 20, 30}
s3.add(40)
print(s3)
#4
s ={"python","java"}
s.add("java script")
s.add("c++")
print(s)
#5
s={100, 200, 300, 400}
s.remove(300)
print(s)
#6
frutii = {"apple","mango","banana"}
if "mango" in frutii:
    print("mango exists")
else:
    print("does not ")
#7
set1 = {1, 2, 4, 5}
set1.clear()
print(set1)
#8
set1 = {10, 20, 30, 40, 50,345}
set2 = {100, 20, 303, 40}
sett = set1.intersection(set2)
print(sett)
#9
sett2 = set1.union(set2)
print(sett2)
#10
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}
C = A.difference(B)
print(C)
#11
D = A.symmetric_difference(B)
print(D)
#12
sset = {10,20,30,10,20,40,50}
#13
