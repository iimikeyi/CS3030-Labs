import re
import csv

PATTERN = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (ERROR) (.+)"

errors = []

with open("../task1/sample.log", "r") as f:
    for line in f:
        match = re.search(PATTERN, line)
        if match: 
            errors.append([match.group(1), match.group(2), match.group(3)])

with open("error_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Error Type", "Message"])
    writer.writerows(errors)

print(f"Done! {len(errors)} errors written to error_report.csv")