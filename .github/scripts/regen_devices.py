import json
import os

device_list = []

for device in os.listdir("API/devices"):
    with open(f"API/devices/{device}", "r") as f:
        device_data = json.load(f)

    device_entry = {
        "codename": device_data["codename"],
        "codename_alt": device_data["codename_alt"],
        "vendor": device_data["vendor"],
        "model": device_data["model"],
        "maintainer_name": " && ".join(
            [maintainer["display_name"] for maintainer in device_data["maintainer"]]
        ),
        "frame": None,
        "active": device_data["active"],
    }

    device_list.append(device_entry)

# sort the device list based on codenames
device_list.sort(key=lambda x: x["codename"])

devices_json = {"devices": device_list}

with open("API/devices.json", "w") as f:
    json.dump(devices_json, f, indent=4)
