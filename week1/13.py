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

class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name = name 
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    @staticmethod
    def college():
        print('yo! student from BIAS')

    def avg(self):
        avg = (self.sub1+self.sub2+self.sub3)/3  
        return avg  
    def __str__(self):
        return f'{self.name} has an average of {self.avg()}'

s1 = Student('Kartik Budhlakoti' , 60,60,60)
print(s1)
Student.college()
# del s1
# print(s1)

class Person:
    # __name = 'anonymous'

    def __hello(self):
        print(f'Hello Person!!')
    def welcome(self):
        self.__hello()
p1= Person()
print(p1.welcome())