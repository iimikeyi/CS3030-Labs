import psutil
import datetime
import time

CPU_WARN    = 80
RAM_WARN_GB = 1.0
DISK_WARN   = 90

def check():
    cpu  = psutil.cpu_percent(interval=1)
    ram  = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    ram_available_gb = ram.available / (1024 ** 3)

    print(f"--- {datetime.datetime.now()} ---")
    print(f"CPU:  {cpu}%")
    print(f"RAM:  {ram_available_gb:.1f} GB available")
    print(f"Disk: {disk.percent}% used")

    if cpu > CPU_WARN:
        print(f"WARNING: CPU is high ({cpu}%)")
    if ram_available_gb < RAM_WARN_GB:
        print(f"WARNING: Low RAM ({ram_available_gb:.1f} GB left)")
    if disk.percent > DISK_WARN:
        print(f"WARNING: Disk almost full ({disk.percent}% used)")

while True:
    check()
    time.sleep(60)
