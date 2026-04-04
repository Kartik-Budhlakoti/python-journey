import glob
import shutil
import os
from pathlib import Path
os.makedirs('archive', exist_ok=True)
for file_name in glob.glob('*.py'):
    new_path = os.path.join('archive', file_name)
    shutil.copy2(file_name , new_path)

p = Path.cwd()
print(p)
p = Path.home()
print(p)
p = Path('/home/kartik007/Desktop/python-new/python-journey/month2/1.py')
print(p)

print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)

print(p.exists())
print(p.is_dir())
print(p.is_file())

for item in p.iterdir():
    print(item)

for py_file in p.rglob('*.py'):
    print(py_file)

for f in p.iterdir():
    if f.is_file():
        print(f.name, f.stat().st_size)

print(f'You can find me here: {Path(__file__).parent}')

# for file_path in Path.cwd().glob('*.py'):
#     new_path = Path('month2') / 'archive' / file_path.name
#     file_path.rename(new_path)