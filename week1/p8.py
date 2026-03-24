from pathlib import Path
# p = Path.cwd()
# print(p)
# with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'w') as f:
#     f.write('kartik\n')
#     f.write('budhlakoti\n')
#     f.write('Btech\n')
#     f.write('Cse\n')
#     f.write('3rd year\n')
# print(f)
# with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'r') as f:
#     print(f.read())

# with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'a') as f:
#     f.write('This program was run.')

# with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'r') as f:
#     i=1
#     for line in f:
#         print(f'line {i}: {line.strip()}')
#         i += 1
#     for i ,line in enumerate(f,start = 1):
#         print(f'line {i}: {line.strip()}')

with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'w') as f:
    f.write('Kartik , 85\n')
    f.write('Amit , 62\n')
    f.write('Priya , 91\n')
    f.write('Rahul , 55\n')
students = {}
with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            name, score = line.split(',')
            students[name] = int(score)
scores = list(students.values())
highest = max(scores)
lowest = min(scores)
average = sum(scores)/len(scores)
print(f'Highest : {max(students, key= students.get)} ({highest})')
print(f'Lowest : {min(students, key= students.get)} ({lowest})')
print(f'Average : {average}')
print('All scores : ')
for name,score in sorted(students.items()):
    print(f'  {name}: {score} ')

import re
unique = []
with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'r') as f:
    mail = re.compile(r'\w+@gmail.com')
    for line in f:
        mo = mail.search(line)
        if mo:
            if mo.group() not in unique:
                unique.append(mo.group())
print(len(unique))
        
# with open('/home/kartik007/Desktop/python-new/python-journey/week1' , 'r') as f:
#     for files in f:
#         text_files = re.compile(r'*.txt')
#         name = text_files.search(files)
#         print(name.group())
#         print(Path(files).stat().st_size)
#         count = 0
#         for line in files:
#             count += 1
#         print(count)
# with open('/home/kartik007/Desktop/python-new/python-journey/week1/summary.txt' , 'a') as f:
#     f.write()