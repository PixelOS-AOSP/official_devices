import shutil
import os
import json
import datetime

codename = os.environ["codename"]
version_string = os.environ["version_string"]
current_date = datetime.date.today().strftime("%d %B %Y")

# Copy updater json as it is from releases
# copy2 overwrites the destination file
shutil.copy2(f"releases/{codename}.json", f"API/updater/{codename}.json")

with open(f"API/updater/{codename}.json", "r") as f:
    updater_data = json.load(f)
    download_link = updater_data["response"][0]["url"]

# Update devices json
with open(f"API/devices/{codename}.json", "r") as f:
    data = json.load(f)

data.update(
    {
        "version": version_string,
        "last_updated": current_date,
        "download_link": download_link,
        "archive": f"https://sourceforge.net/projects/pixelos-releases/files/{version_string}/{codename}/",
    }
)

with open(f"API/devices/{codename}.json", "w") as f:
    json.dump(data, f, indent=4)
