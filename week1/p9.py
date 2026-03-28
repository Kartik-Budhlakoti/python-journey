import shutil
from pathlib import Path
import os 
import zipfile

# current = Path.cwd()
# backup = current / 'backup'

# backup.mkdir(exist_ok=True)
# print(f'Backup folder created : {backup}')

# copied_count = 0

# for py_file in current.glob('*.py'):
#     dest = backup / py_file.name
#     shutil.copy2(py_file, dest)
#     print(f'copied : {py_file.name}')
#     copied_count += 1
# print('Backup complete. ' , copied_count ,' no. of files were copied')
# print('BACKUP LOCATION : ',backup)

# current = Path('/home/kartik007/Desktop/python-new/python-journey')
# new  = current / 'TXT_files'
# new.mkdir(exist_ok=True)

# for i in range(1,5):
#     filename = current / f'file{i}.txt'
#     filename.write_text(f'This is content for file{i}.txt')
#     print(f'Created: file{i}.txt')

# for txt_files in current.glob('*.txt'):
#     shutil.move(txt_files , new / txt_files.name)
#     print(f'File moved : {txt_files.name}')

# curr = Path('/home/kartik007/Desktop/python-new/python-journey')
# for root , dirs , files in os.walk(curr):
#     print(f'The folder is {root}')
#     if 'venv' in dirs:
#         dirs.remove('venv')
#     if '.git' in dirs:
#         dirs.remove('.git')  
#     for subfolder in dirs:
#         print(f'  Subfolders of {root} are : {subfolder}')
#     for filename in files:
#         print(f'    Files are : {filename}')

# print('\nDone..')

# messy = Path('/home/kartik007/Desktop/python-new/python-journey/messy_folder')
# messy.mkdir(exist_ok=True)
# for folder in ['allpy', 'alltxt', 'allzip', 'other_subfolder']:
#     (messy / folder).mkdir(exist_ok=True)
# counts = {'allpy':0, 'alltxt':0, 'allzip':0 , 'other_subfolder' : 0}
# for root, dirs, files in os.walk(messy):
#     for filename in files:
#         fullpath = os.path.join(root , filename)

#         if filename.endswith('.py'):
#             dest = messy / 'allpy' / filename
#             shutil.move(fullpath , dest)
#             counts['allpy'] +=1 
#             print(f'Moved {filename} to dest')
#         elif filename.endswith('.txt'):
#             dest = messy / 'alltxt' / filename
#             shutil.move(fullpath , dest)
#             counts['alltxt'] += 1
#             print(f'Moved {filename} to dest')
#         elif filename.endswith('.zip'):
#             dest = messy / 'allzip' / filename
#             shutil.move(fullpath , dest)
#             counts['allzip'] += 1
#             print(f'Moved {filename} to dest')
#         else:
#             dest = messy / 'other_subfolder' / filename
#             shutil.move(fullpath , dest)
#             counts['other_subfolder'] += 1
#             print(f'Moved {filename} to dest')

# print('\nSummary: ')
# for folder, count in counts.items():
#     print(f'{folder} : {count} files')

import send2trash
send2trash.send2trash('/home/kartik007/Desktop/python-new/python-journey/messy_folder')

with zipfile.ZipFile('/home/kartik007/Desktop/python-new/python-journey/backup.zip' , 'w') as zf:
    
    filelist = []
    smallfile = []
    for root, dirs, files in os.walk('/home/kartik007/Desktop/python-new/python-journey'):
        for filenames in files:
            fullpath = os.path.join(root , filenames)
            if filenames.endswith('.txt'):
                if Path(fullpath).stat().st_size > 100:
                    filelist.append(filenames)
                    zf.write(fullpath, os.path.relpath(fullpath , '/home/kartik007/Desktop/python-new/python-journey'))
                else:
                    smallfile.append(filenames)
    print(filelist, smallfile)
