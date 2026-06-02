from pathlib import Path
target_directory = '.'
for file in Path(target_directory).rglob("*.tmp"):
    print(f"Found Junk: {file}")

    