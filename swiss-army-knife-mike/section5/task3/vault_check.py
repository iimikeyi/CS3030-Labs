import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="../../.env")

key = os.getenv("SUPER_SECRET_KEY")

if key:
    masked = "*" * (len(key) - 3) + key[-3:]
    print(f"Accessing system with key: {masked}")
else:
    print("[ERROR] SUPER_SECRET_KEY not found in environment.")
