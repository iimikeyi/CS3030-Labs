import psutil
import datetime

CPU_WARN    = 80 
RAM_WARN_GB = 1.0
DISK_WARN   = 90


cpu  = psutil.cpu_percent(interval=1)
ram  = psutil.virtual_memory()
disk = psutil.disk_usage("/")

ram_available_gb = ram.available / (1024 ** 3)

print(f"--- {datetime.datetime.now()} ---")
print(f"CPU: {cpu}%")
print(f"RAM: {ram_available_gb:.1f} GB available")
print(f"Disk: {disk.percent}% used")

if cpu > CPU_WARN: 
	print(f"\033[91mWARNING: CPU is high ({cpu}%)\033[0m")

if ram_available_gb < RAM_WARN_GB:
	print(f"\033[91mWARNING: Low RAM ({ram_available_gb:.1f} GB left)\033[0m")

if disk.percent > DISK_WARN:
	print(f"\033[91mWARNING: Disk almost full ({disk.percent}%)\033[0m")

