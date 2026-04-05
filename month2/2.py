from pathlib import Path
import os 
import datetime

new_dir = Path(Path.cwd())
new_dir.mkdir(parents=True ,exist_ok=True)
print(new_dir)
test_file = new_dir / '3.py'
test_file.write_text('temporary')
test_file.unlink()
# new_dir.rmdir() only works if dir is empty

project = Path('/home/kartik007/Desktop/python-new/python-journey')
for f in project.rglob('2.py'):
    print(f)
project = Path(Path.cwd())
for f in project.glob('*.py'):
    print(f)
for f in project.rglob('*.py'):
    if 'venv' not in f.parts and '__pycache__' not in f.parts:
        print(f)

f = Path('/home/kartik007/Desktop/python-new/python-journey/README.md')
stat = f.stat()
print(f'size in bytes is {stat.st_size}')
print(f'size in KB is {stat.st_size / 1024:.2f} KB')
mod_time = datetime.datetime.fromtimestamp(stat.st_mtime)
print(f'Last modified: {mod_time.strftime('%Y-%m-%d %H:%M:%S')}')
print(f'Permissions: {oct(stat.st_mode)}')

filepath = '/home/kartik007/Desktop/python-new/python-journey/README.md'
# os
print(os.path.exists(filepath))
print(os.path.isfile(filepath))
print(os.path.basename(filepath))
print(os.path.dirname(filepath))
print(os.path.join('/home/kartik007', 'Desktop', 'python-new' , 'python-journey' , 'file1.txt'))
# pathlib
p=Path(filepath)
print(p.exists())
print(p.is_file())
print(p.stem)
print(p.parent)
print(p.stat().st_size)
print(Path('/home/kartik007/Desktop/python-new') / 'python-journey' / 'file1.txt')