# class Student:
#     college = 'Birla institute of applied sciences bhimtal'
#     def __init__(self,name , year ,cgpa):
#         self.name = name
#         self.year = year
#         self.cgpa = cgpa
#     def introduce(self):
#         print(f'Hi I am {self.name}, {self.year} year student with CGPA {self.cgpa}')
#     def is_passing(self):
#         return self.cgpa >= 6.0
# kartik = Student('KARTIK BUDHLAKOtI', '3rd' , 6.5)
# kartik.introduce()
# print('at  ',kartik.college)
# print(kartik.is_passing())

# class Parent:
#     speaks = ['Hindi']
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.speaks = Parent.speaks + ['English']
#         print(self.speaks)
# c = Child()

# class Dog:
#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
    
# miles = Dog('Miles', 4, 'jack russell')
# buddy = Dog('Buddy', 8, 'bulldog')
# jack = Dog('Jack', 7, 'Cane Corso')
# miles.speak('Yap')
# buddy.speak('Woof')
# jack.speak('meow')  
# print(miles)   

# class Dog:
#     species = 'Canis familiaris'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f'{self.name} is {self.age} years old'
#     def speak(self, sound):
#         return f'{self.name} says {sound}'
# class JackRussellTerrier(Dog):
#     pass

# class Dachshund(Dog):
#     pass

# class Bulldog(Dog):
#     pass
# miles = JackRussellTerrier('Miles', 4)
# buddy = Dachshund('Buddy', 9)
# jack = Bulldog('Jack', 3)
# jim = Bulldog('Jim', 5)
# print(miles.species)
# print(buddy.name)
# print(jack)
# jim.speak('woof')
# print(type(miles))

# class Student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name = name 
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3

#     @staticmethod
#     def college():
#         print('yo! student from BIAS')

#     def avg(self):
#         avg = (self.sub1+self.sub2+self.sub3)/3  
#         return avg  
#     def __str__(self):
#         return f'{self.name} has an average of {self.avg()}'

# s1 = Student('Kartik Budhlakoti' , 60,60,60)
# print(s1)
# Student.college()
# del s1
# print(s1)

# class Person:
#     # __name = 'anonymous'

#     def __hello(self):
#         print(f'Hello Person!!')
#     def welcome(self):
#         self.__hello()
# p1= Person()
# print(p1.welcome())

class Car:
    @staticmethod
    def start():
        return 'Car started'
    @staticmethod
    def stop():
        return 'Car stopped'

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return self.brand

class FacLoc(ToyotaCar):
    def __init__(self, location):
        self.location = location
    def __str__(self):
        return self.location
    

car1 = ToyotaCar('Fortuner')
print(f" {car1.name} {car1.start()}")
car2 = ToyotaCar('Supra')
print(f" {car2.name} {car2.start()}")

brd1 = ToyotaCar('Supra')
con1 = FacLoc('Haldwani')
print(f'{brd1} has a factory in {con1.location} and the {brd1.start()}...')

class A:
    varA = 'Welcome to class A'
class B:
    varB = 'Welcome to class B'
class C(A,B):
    varC = 'Welcome to class C'

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

class Person:
    name = 'anonymous'
    def changename(self , name):
        # self.name = name
        self.__class__.name = name
       # or Person.name = name
    @classmethod
    def changename(cls, name):
        cls.name = name

p1 = Person()
p1.changename('John')
print(p1.name)
print(Person.name)

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    #     self.percentage = str((self.phy +self.chem + self.maths)/3) + '%'

    # def calcPercentage(self):
    #     self.Percentage = str((self.phy +self.chem + self.maths)/3) + '%'
    # or

    @property
    def percentage(self):
        return str((self.phy +self.chem + self.maths)/3) + '%'
    
std1 = Student(88,34,75)
print(std1.percentage)
std1.phy = 45
print(std1.percentage)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def shownumber(self):
        print(self.real,'i + ',self.img,'j')

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1,2)
num1.shownumber()
num2 = Complex(3,4)
num2.shownumber()

# num3 = num1.add(num2)
num3 = num1 + num2
num3.shownumber()

num4 = num2 - num1
num4.shownumber()