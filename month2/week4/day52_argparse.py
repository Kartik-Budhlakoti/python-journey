import argparse
#    ----- pattern -----
# 1- Create parser
# 2- Add arguments
# 3- Parse arguments
# 4- Use arguments

parser = argparse.ArgumentParser(
    description="Argparse practice script",
    epilog="Example: python  day52_argparse.py --name Kartik --age 20"
)
#  Positional argument - required, no -- prefix
#  User runs: python script.py Kartik

parser.add_argument(
    'name',
    type=str,
    help='Your name'
)
#  Optional argument - not required, has -- prefix
#  User runs: python script.py Kartik --age 20

parser.add_argument(
    '--age',                   # here "--" is the reason for bashing
    type=int,                  #  "--name" instead of "name"
    default = 0,
    help="Your age (default 0)"
)
#  Flag argument - no value, present or absent
#  User runs: python script.py Kartik --verbose

parser.add_argument(
    "--verbose",
    action="store_true",
    help="Print detailed output"
)
#  Choice argument - value must be one of a specific set

parser.add_argument(
    '--level',
    type=str,
    choices=['beginner','intermidiate','advanced'],
    default='beginner',
    help="Your skill level (default beginner)"
)
args = parser.parse_args()

# Accessing the argumnets via args
print(f"Name : {args.name}")
print(f"Age : {args.age}")
print(f"Verbose : {args.verbose}")
print(f"Level : {args.level}")

if args.verbose:
    print(f"\nVerbose mode is ON - printing extra details")
    print(f"Full args object : {args}")