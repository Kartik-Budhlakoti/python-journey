import os 
import shutil
from pathlib import Path
import datetime
import stat

home = os.environ.get('HOME')
print(f'Home : {home}')
path = os.environ.get('PATH')
print(f'Path : {path}')

api_key = os.environ.get('MY_API_KEY', 'not_set')
print(f'API KEY : {api_key}')
os.environ['MY_TEST_VAR'] = 'hello'
print(os.environ.get('MY_TEST_VAR'))

print(os.getcwd())
# os.chdir('/home/kartik007/Desktop/python-new/python-journey') for the directory's values
os.chdir('/home/kartik007/Desktop/python-new/python-journey/week1')

print(os.getcwd())

items = os.listdir('.')
for item in items:
    print(item)

for item in os.listdir('.'):
    if 'venv' not in item:
        full_path = os.path.join(os.getcwd(),item)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            print(f'File : {item} ({size} bytes)')
        elif os.path.isdir(full_path):
                print(f'DIR: {item} ({os.path.getsize(full_path)} bytes)')

for folder_path, subfolders, filenames in os.walk('/home/kartik007/Desktop/python-new/python-journey'):
    subfolders[:] = [d for d in subfolders
                     if d not in ['venv', '.git', '__pycache__']]

    print(f'\nFolder: {folder_path}')
    for filename in filenames:
        full_path = os.path.join(folder_path , filename)
        size = os.path.getsize(full_path)
        print(f' {filename}  ({size} bytes)')


# Stat module
filepath = '/home/kartik007/Desktop/python-new/python-journey/README.md'
mode = os.stat(filepath).st_mode
print(f'Raw mode : {oct(mode)}')

print(f'Owner can read  :      {bool(mode & stat.S_IRUSR)}')
print(f'Owner can write  :     {bool(mode & stat.S_IWUSR)}')
print(f'Owner can execute  :   {bool(mode & stat.S_IXUSR)}')
print(f'Group can read  :      {bool(mode & stat.S_IRGRP)}')
print(f'Others can read  :     {bool(mode & stat.S_IROTH)}')
print('\n')
os.chmod(filepath, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP)
print(f'Owner can read  :      {bool(mode & stat.S_IRUSR)}')
print(f'Owner can write  :     {bool(mode & stat.S_IWUSR)}')
print(f'Owner can execute  :   {bool(mode & stat.S_IXUSR)}')
print(f'Group can read  :      {bool(mode & stat.S_IRGRP)}')
print(f'Others can read  :     {bool(mode & stat.S_IROTH)}')