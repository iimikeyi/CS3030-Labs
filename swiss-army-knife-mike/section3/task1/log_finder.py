import re 

IP_PATTERN        = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
TIMESTAMP_PATTERN = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]"

with open("sample.log", "r") as f:
    contents = f.read()

ip_addresses = re.findall(IP_PATTERN, contents)
timestamps   = re.findall(TIMESTAMP_PATTERN, contents)

print(f"TIMESTAMPS FOUND ({len(timestamps)}):")
for ts in timestamps: 
    print(f" {ts}")

print(f"IP ADDRESSES FOUND ({len(ip_addresses)}):")
for ip in ip_addresses:
    print(f" {ip}")