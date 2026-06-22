"""#herachical
class Father:
    def __init__(self):
        self.fname="abc"
    def father(self):
        print(f"Father name is {self.fname}")

class Child1(Father):
    def __init__(self):
        Father.__init__(self)
        self.cname="samm"
    def child(self):
        print(f"first child name is {self.cname}")

class Child2(Father):
    def __init__(self):
        Father.__init__(self)
        self.cname="sneh"
    def child2(self):
        print(f"Second child name is {self.cname}")
c1=Child1()
c1.child()
c1.father()

c2=Child2()
c2.child2()
c2.father()

#hybrid
class School:
    def school(self):
        print("This is the school class method")
class student1(School):
    def show1(self):
        print("this is the student 1st calss")
class student2(School):
    def show2(self):
        print("this is the student 2nd calss")
class student3(student1,School):
    def show3(self):
        student2.show2(self)
        print("this is the student 3rd calss")
s=student3()
s.school()
s.show1()
s.show3()"""


"""
#polymorphism
#method overridding
class vehical:
    def Display(self):
        print("this is class vehical method")
class bus(vehical):
    def Display(self):
        super().Display()
        print("Bus is road transport mode vehical")
b=bus()
b.Display()
"""

#Encapsulation
class parent:
    def __init__(self):
        self.__a=10 #private
        self._b=20 #protected
    def Details(self):
        print("value of a in parent clas is",self.__a)
class Child(parent):
    def __init__(self):
        super().__init__()
    def Show(self):
        #print("value of a in child class is",self.__a)
        print("value of a in child class is",self._b)

obj=Child()
obj.Details()
obj.Show()
print(obj._b)

#abstraction
#concret ?
from abc import ABC, abstractmethod
class vehical(ABC):
    def __init__(self):
        self.model_name="creta"
        self.year=2000
    @abstractmethod
    def Details(self):
        pass
class car(vehical):
    def __init__(self):
        super().__init__()
    def Details(self):
        print("Model name is",self.model_name)
        print("Year is",self.year)
c=car()
c.Details()
