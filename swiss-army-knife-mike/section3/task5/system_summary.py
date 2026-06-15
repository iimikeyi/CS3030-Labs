import subprocess
import re

result = subprocess.run(["ps", "aux"], capture_output=True, text=True)

if not result.stdout.strip():
    print("Error: no login data available (WSL limitation)")
    exit()

pattern = r"(\S+)\s+(pts/\d+)\s+(\d{4}-\d{2}-\d{2} \d{2}:\d{2})"
rows = re.findall(pattern, result.stdout)

print("=" * 55)
print("         SYSTEM LOGIN DASHBOARD")
print("=" * 55)
print(f"{'USER':<15} {'TERMINAL':<12} {'LOGIN TIME'}")
print("-" * 55)
for user, terminal, time in rows:
    print(f"{user:<15} {terminal:<12} {time}")
print("=" * 55)
print(f"  Total sessions: {len(rows)}")
print("=" * 55)