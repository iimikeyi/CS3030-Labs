def read_lines(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield line.strip()

def find_keyword(filepath, keyword):
    print(f"Scanning for: {keyword}\n")
    found = 0
    for line in read_lines(filepath):
        if keyword in line:
            print(f"  MATCH → {line}")
            found += 1
    print(f"\nDone. {found} match(es) found.")

if __name__ == "__main__":
    find_keyword("../task1/sample.log", "CRITICAL")