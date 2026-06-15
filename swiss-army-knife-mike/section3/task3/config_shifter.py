import json
import yaml

config = {
    "server": "prod",
    "port": 80,
    "status": "active",
    "tags": ["web", "linux"]
}

with open("config.json", "w") as f:
    json.dump(config, f, indent=4)
print("config.json written")

with open("config.json", "r") as f:
    data = json.load(f)

data["status"] = "maintenance"

with open("config.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)
print("config.yaml written")
