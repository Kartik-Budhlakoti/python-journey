import os
from pathlib import Path
# for filename in Path.home().glob('*.txt'):
#   # os.unlink(filename)
    # print('Deleting : ', filename)

# print(os.listdir(r'/home/kartik007/Desktop/python-new/python-journey/week1'))

import os , shutil
h = Path.home()
for folder_name, subfolders, filenames in os.walk(h / 'spam'):
    print('The current folder is '+ folder_name)
    
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': '+ subfolder)
    
    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': '+ filename)
        p = Path(folder_name)
        shutil.move(p / filename, p / filename.upper())
        
    print('')