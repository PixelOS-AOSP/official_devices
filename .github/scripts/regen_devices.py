import json
import os

device_list = []

for device in os.listdir("API/devices"):
    with open(f"API/devices/{device}", "r") as f:
        device_data = json.load(f)

    codename = device_data["codename"]
    updater_path = f"API/updater/{codename}.json"
    last_updated = None
    version = None
    if os.path.exists(updater_path):
        with open(updater_path, "r") as f:
            updater_data = json.load(f)
            if len(updater_data.get("response", [])) > 0:
                try:
                    last_updated = int(updater_data["response"][0].get("datetime"))
                    version = int (updater_data["response"][0].get("version"))
                except:
                    pass

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
        "last_updated": last_updated,
        "version": version,
    }

    device_list.append(device_entry)

# sort the device list based on codenames
device_list.sort(key=lambda x: x["codename"])

devices_json = {"devices": device_list}

with open("API/devices.json", "w") as f:
    json.dump(devices_json, f, indent=4)

# Generate Device List Markdown
active_devices = [d for d in device_list if d["active"]]

# Group devices by brand
brand_devices = {}
for device in active_devices:
    brand_devices.setdefault(device["vendor"], []).append(device)

sorted_brands = sorted(brand_devices.keys())

# Construct Markdown content
lines = [
    "# Device List",
    "Here is the list of all the devices actively supported officially by PixelOS. To download the latest version of PixelOS, please visit our official website at [PixelOS.net](https://PixelOS.net), there you can find the necessary resources and information to download and install PixelOS on your device.\n",
    f"Number Of Devices in Official PixelOS: {len(active_devices)}\n",
    f"Number of Brands in Official PixelOS: {len(sorted_brands)}\n",
    "Officially Supported Devices:",
]

for brand in sorted_brands:
    lines.append(f"\n**{brand}**")
    brand_devices[brand].sort(key=lambda x: x["model"])
    for idx, device in enumerate(brand_devices[brand], 1):
        lines.append(f"{idx}. {device['model']} ({device['codename_alt']})")

lines.append(
    "\nWe hope you enjoyed the project! Your donations help us maintain our infrastructure and continue our work. Please consider showing your support by donating! [Click Me](https://blog.pixelos.net/docs/donate/)"
)

with open("docs/DeviceList.md", "w") as f:
    f.write("\n".join(lines))
