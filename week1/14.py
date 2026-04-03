class Student:
    college_name = 'BIAS'
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def introduce(self):
        print(f'Hi I am {self.name}, {self.age} years old, CGPA: {self.cgpa}')
    
    def is_passing(self):
        return self.cgpa>= 6.0
    
    def update_cgpa(self, new_cgpa):
        if Student.is_valid_cgpa(new_cgpa):
            self.cgpa = new_cgpa
            print(f'CGPA updated to {new_cgpa}')
        else:
            print('INVALID CGPA')

    @classmethod
    def from_string(cls, student_string):
        parts = student_string.split(',')
        return cls(parts[0], int(parts[1]), float(parts[2]))
    @staticmethod
    def is_valid_cgpa(cgpa):
        return 0.0<=cgpa<=10.0 

    def __str__(self):
        return f'Student({self.name}, CGPA: {self.cgpa})'

    def __eq__(self, other):
        return self.name == other.name and self.cgpa == other.cgpa

class CollegeStudent(Student):
    def __init__(self, name, age, cgpa, branch, semester):
        super().__init__(name, age, cgpa)
        self.branch = branch
        self.semester = semester
    def introduce(self):
        print(f'Hi I am {self.name}, {self.branch} branch, semester {self.semester}, CGPA: {self.cgpa}')
    
    def study_info(self):
        print(f'{self.name} | Branch: {self.branch} | Semester: {self.semester}')

class BTechStudent(CollegeStudent):
    def __init__(self, name, age, cgpa, branch, semester, project):
        super().__init__(name, age, cgpa, branch, semester)
        self.project = project

    def project_info(self):
        print(f"{self.name}'s project: {self.project}")

print('=== Basic Student ===')
kartik = Student('Kartik Budhlakoti', 20, 6.5)
kartik.introduce()
print(kartik)
print(f'Passing: {kartik.is_passing()}')
kartik.update_cgpa(8.0)

print('\n=== from String ===')
amit= Student.from_string('Amit,21,7.2')
amit.introduce()

print('\n === Static method ===')
print(Student.is_valid_cgpa(6.5))
print(Student.is_valid_cgpa(11.0))

print('\n === Equality ===')
s1 = Student('test', 20 , 7.0)
s2 = Student('test', 20, 7.0)
print(f's1 = s2 : { s1==s2 }')

print('\n === Inheritance ===')
priya = CollegeStudent('Priya', 20, 8.1, 'CS', 6)
priya.introduce()
priya.study_info()
print(f'Passing: {priya.is_passing()}')

print('\n === Multi level Inheritance ===')
rahul = BTechStudent('Rahul', 21,7.5,'CS', 7, 'Devsecops Pipeline')
rahul.introduce()
rahul.study_info()
rahul.project_info()

print('\n Class variable ===')
print(f'College : {Student.college_name}')
print(f'College via object: {kartik.college_name}')