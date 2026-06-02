import subprocess

result = subprocess.run(["df", "-h"], capture_output=True, text=True)

lines = result.stdout.splitlines()

for line in lines:
    if line.endswith(" /") or line.endswith("/mnt/c"):
        print("Disk Report:")
        print(line)