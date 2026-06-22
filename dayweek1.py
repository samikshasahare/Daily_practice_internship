tuple1 = (23, 78, 57, 89)
print(type(tuple1))
print(tuple1[::-1])
t1 = (34, 45, 65, 78)
l1 = list(t1)
print(l1)
l2 = (34, 45, 65, 78)
print(tuple(l2))
t=tuple(range(5,51,5))
print(t)
t1 = (2, 4, 3, 5 ,3)
t2 = (9, 7, 6, 0)
t3 = t1+t2
print(t3)
print(t1*5)
t1 = (20, 40, 30, 50, 300, 30, 40, 20, 40, 30)
print(t1.count(3))
print(max(t1))
print(min(t1))
print(t1.index(30))
print(sorted(t1))
print(sorted(t1,reverse=True))
#tuple paking and un paking
t1="s"
t2=3
t3=4.5
tu=t1,t2,t3
print(tu)
t4 = ("sam",7,1,44.6)
a,b,c,d=t4
print("a:",a,"b:",b,"c:",c,"d:",d)
even =[x*1 for x in range(101) if x%2==0]
print(even)
#
"""m1 = input("enter 1st")
m2 = input("enter 3st")
m3 = input("enter 3st")
movie = m1,m2,m3
print(movie)"""

#wp to covert list and tuple into set
tuple1 = (34, 45, 65, 78)
print(set(tuple1))
list1 = [34, 45, 65, 78]
print(set(list1))
print(type(tuple1))
print(type(list1))