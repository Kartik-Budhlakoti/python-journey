class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        ar = 3.14 * (self.radius**2)
        return ar
    def perimeter(self):
        peri = 2* 3.14 * self.radius
        return peri
c1 = Circle(10)
print(c1.area())
print(c1.perimeter())

class Employee:
    def __init__(self,role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print('role = ', self.role)
        print('dept = ', self.dept)
        print('salary = ', self.salary)

class Engineer(Employee):
    def __init__(self,name, age):
        self.name = name
        self.age = age
        super().__init__('Engineer', 'RND' , 123456789)


emp1 = Engineer('kartik' , 20)
emp1.showDetails()

class Order:
    def __init__(self, item , price):
        self.item = item
        self.price = price
    def __gt__(self, odr2):
        return self.price > odr2.price

odr1 = Order('Milk' , 30)
odr2 = Order('Egg' , 7)
print(odr1 > odr2)