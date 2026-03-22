from pathlib import Path
# home = Path.home()
# print(home)
# cwd = Path.cwd()
# print(cwd)
# my_path = Path('/home/kartik007/Desktop/python-new/python-journey/week1')
# print(my_path)
# file_path = Path('/home/kartik007/Desktop/python-new/python-journey') / 'week1' / 'tests.txt'
# print(file_path)

# p = Path('/home/kartik007/Desktop/python-new/python-journey/week1/tests.txt')
# print(p.name)
# print(p.stem)
# print(p.suffix)
# print(p.parent)
# print(p.exists())
# print(p.is_file())
# print(p.is_dir())

# print(p.stat().st_size)------> will work without the 'tests.txt'

# for f in Path('/home/kartik007/Desktop/python-new/python-journey/week1').iterdir():
#     print(f.stat().st_size)

# p = Path('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt')
# p.write_text('Hello from Python \nThis is line 2\nThis is line 3')
# content = p.read_text()
# print(content)

# with open('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt' , 'w') as f:
#     f.write('First line\n')
#     f.write('Second line\n')
#     f.write('Third line\n')
# with open('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt' , 'r') as f:
#     content = f.read()
#     print(content)
# with open('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt' , 'r') as f:
#     for line in f:
#         print(line.strip())
# with open('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt' , 'r') as f:
#     lines = f.readlines()
#     print((lines))
# with open('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt' , 'a') as f:
#     f.write('This line was added later\n')
# with open('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt' , 'r') as f:
#     for line in f:
#         print(line.strip())

# file_path = Path('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt')
# try:
#     content = file_path.read_text()
#     print(content)
# except FileNotFoundError:
#     print(f'Error: {file_path} does not exist')

# import shelve 
# with shelve.open('/home/kartik007/Desktop/python-new/python-journey/week1/mydata.db') as db:
#     db['name'] = 'kartik'
#     db['scores'] = [65,98,88]
#     db['settings'] = {'theme':'dark', 'language': 'python'}

# with shelve.open('/home/kartik007/Desktop/python-new/python-journey/week1/mydata.db') as db:
#     print(db['name'])
#     print(db['scores'])
#     print(db['settings'])

# folder = Path('/home/kartik007/Desktop/python-new/python-journey/week1')
# for py_file in folder.glob('*.py'):
#     print(py_file.name)

import datetime
p = Path('/home/kartik007/Desktop/python-new/python-journey/week1/notes.txt')
mod_time = datetime.datetime.fromtimestamp(p.stat().st_mtime)
print(f'Last modified : {mod_time}')