import requests
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path="../.env")

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

def send_alert(message):
        payload = {"content": message}
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204:
                print(f"Alert sent: {message}")
        else:
                print(f"Failed to send alert (status: {response.status_code})")

alerts = []

cpu_pct = 85
ram_gb = 0.4
disk_pct = 95

if cpu_pct > 80:
    alerts.append(f"WARNING: CPU is high ({cpu_pct}%)")

if ram_gb < 1.0:
    alerts.append(f"WARNING: Low RAM ({ram_gb} GB available)")

if disk_pct > 90:
    alerts.append(f"WARNING: Disk almost full ({disk_pct}% used)")

if alerts:
    for alert in alerts:
        send_alert(alert)
else:
    send_alert("Heartbeat check: all systems nominal.")
