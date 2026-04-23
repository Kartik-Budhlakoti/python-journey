import sys
from pathlib import Path

# if (args_count :=  len(sys.argv)) >2 :
#     print(f"One argument expected , got {args_count - 1}")
#     raise SystemExit(2)
# elif args_count < 2:
#     print(f"You must specify the target directory path")
#     raise SystemExit(2)

# print(f"\nArguments count is : {args_count} \n")

# target_dir = Path(sys.argv[1])

# if not target_dir.is_dir():
#     print(f"The targeted dir {target_dir} doesn't exist")
#     raise SystemExit(1)
# for entry in target_dir.iterdir():
#     print(entry.name)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path")
args= parser.parse_args()
target_dir = Path(args.path)
if not target_dir.exists():
    print(f"This {target_dir} doesn't exist")
    raise SystemExit(1)
saver = Path('/home/kartik007/Desktop/python-new/python-journey/month2/week4/practice-save')
names = []
for element in target_dir.iterdir():
    names.append(element.name)

saver.write_text("\n".join(names))