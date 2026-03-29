class Student:
    college = 'Birla institute of applied sciences bhimtal'
    def __init__(self,name , year ,cgpa):
        self.name = name
        self.year = year
        self.cgpa = cgpa
    def introduce(self):
        print(f'Hi I am {self.name}, {self.year} year student with CGPA {self.cgpa}')
    def is_passing(self):
        return self.cgpa >= 6.0
kartik = Student('KARTIK BUDHLAKOtI', '3rd' , 6.5)
kartik.introduce()
print('at  ',kartik.college)
print(kartik.is_passing())

class Parent:
    speaks = ['Hindi']
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks = Parent.speaks + ['English']
        print(self.speaks)
c = Child()

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    def speak(self, sound):
        return f'{self.name} says {sound}'
    
miles = Dog('Miles', 4, 'jack russell')
buddy = Dog('Buddy', 8, 'bulldog')
jack = Dog('Jack', 7, 'Cane Corso')
miles.speak('Yap')
buddy.speak('Woof')
jack.speak('meow')  
print(miles)   