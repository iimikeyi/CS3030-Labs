import argparse
from pathlib import Path
parser = argparse.ArgumentParser(
    description="A recursive file finder. Search any folder for any file type."
)

parser.add_argument(
    "--path",
    required=True,
    help="The directory path you want to scan"
)

parser.add_argument(
    "--ext",
    required=True,
    help="The file extension to search for (e.g. .tmp, .py, .txt)"
)

args = parser.parse_args()

ext = args.ext if args.ext.startswith(".") else f".{args.ext}"

print(f"\nSearching in: {args.path}")
print(f"Looking for: *{ext}\n")

found = list(Path(args.path).rglob(f"*{ext}"))

if found: 
    for file in found: 
        print(f"Found: {file}")
    print(f"\nTotal: {len(found)} file(s) found.")
else: 
    print("No matching files found.")