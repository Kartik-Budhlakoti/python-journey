from pathlib import Path
p = Path.cwd()
print(p)
with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'w') as f:
    f.write('kartik\n')
    f.write('budhlakoti\n')
    f.write('Btech\n')
    f.write('Cse\n')
    f.write('3rd year\n')
print(f)
with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'r') as f:
    print(f.read())

with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'a') as f:
    f.write('This program was run.')

with open('/home/kartik007/Desktop/python-new/python-journey/week1/new_file.txt' , 'r') as f:
    i=1
    for line in f:
        print(f'line {i}: {line.strip()}')
        i += 1
    for i ,line in enumerate(f,start = 1):
        print(f'line {i}: {line.strip()}')
