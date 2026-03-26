import os
from pathlib import Path
# for filename in Path.home().glob('*.txt'):
#   # os.unlink(filename)
    # print('Deleting : ', filename)

# print(os.listdir(r'/home/kartik007/Desktop/python-new/python-journey/week1'))

import shutil
# h = Path.home()
# for folder_name, subfolders, filenames in os.walk(h / 'spam'):
#     print('The current folder is '+ folder_name)
    
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folder_name + ': '+ subfolder)
    
#     for filename in filenames:
#         print('FILE INSIDE ' + folder_name + ': '+ filename)
#         p = Path(folder_name)
#         shutil.move(p / filename, p / filename.upper())
        
#     print('')


shutil.copytree('/home/kartik007/Desktop/python-new/python-journey/week1',
            '/home/kartik007/Desktop/week1.backup')

shutil.copy('/home/kartik007/spam2/file1.txt',
            '/home/kartik007/Desktop/test.txt')
shutil.move('/home/kartik007/Desktop/test.txt', 
            '/home/kartik007/Documents/test.txt')
shutil.move('/home/kartik007/Documents/test.txt',
            '/home/kartik007/Documents/test2.txt')

os.unlink('/home/kartik007/Documents/test2.txt')
shutil.rmtree('/home/kartik007/spam2')
import send2trash
send2trash.send2trash('/home/kartik007/spam_backup/file2.txt')

for folderpath, subfolders, filenames in os.walk('/home/kartik007/Desktop/python-new/python-journey'):
    if 'venv' in subfolders:
        subfolders.remove('venv')
    for filename in filenames :
        if filename.endswith('.py'):
            full_path = Path(folderpath) / filename
            print(full_path)

import zipfile
with zipfile.ZipFile('/home/kartik007/Desktop/python-new/python-journey/week1/example.zip', 'r') as zf:
    print(zf.namelist())
    info = zf.getinfo('file1.txt')
    print(info.filename)
    print(info.file_size)
    print(info.compress_size)
with zipfile.ZipFile('/home/kartik007/Desktop/python-new/python-journey/week1/example.zip', 'r') as zf:
    zf.extractall('/home/kartik007/Desktop/python-new/python-journey/week1/extracted')
    zf.extract('file1.txt', '/home/kartik007/Desktop/python-new/python-journey/week1/extracted')

folder = Path('/home/kartik007/Desktop/python-new/python-journey/week1')
for py_file in folder.glob('*.py'):
    new_name = folder / f'backup_{py_file.name}'
    py_file.rename(new_name)