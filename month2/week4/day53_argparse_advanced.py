import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Advanced argparse patterns"
)
parser.add_argument(
    "--checks",
    nargs="+",      # one or more value
    choices=['disk','memory','processes','network','users'],
    default=['disk','memory','processes','network','users'],
    help="Which checks to run (default all)"
)

# File path argument
parser.add_argument(
    "--output",
    type=str,
    default='report.txt',
    help="Output file path (default report.txt) "
)

# Required argument - no default , must be provided
parser.add_argument(
    "--directory",
    type=str,
    required=True,
    help="Directory to scan (required)"
)
args = parser.parse_args()

directory = Path(args.directory)
if not directory.exists():
    parser.error(f"Directory does not exist : {args.directory}")

print(f"Checks to run : {args.checks}")
print(f"Output file : {args.output}")
print(f"Directory  : {args.directory}")
print(f"Directory exists : {directory.exists()}")