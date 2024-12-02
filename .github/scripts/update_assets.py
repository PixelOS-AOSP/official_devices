import shutil
import os
import json
import datetime

codename = os.environ["codename"]
version_string = os.environ["version_string"]
changelogs = os.environ["changelogs"]

current_date = datetime.date.today()


# Write to changelogs
with open(f"API/devices/{codename}.json", "r") as f:
    old_data = json.load(f)
    old_version = old_data["version"]

if old_version != f"{codename}":
    try:
        # delete changelogs for older versions
        os.remove(f"API/changelogs/{codename}.md")
    except FileNotFoundError:
        print("File does not exist.")

changelogs = "# " + current_date.strftime("%d-%b-%Y") + "\n" + changelogs + "\n"

try:
    with open(f"API/changelogs/{codename}.md", "r") as contents:
        save = contents.read()
except FileNotFoundError:
    save = ""

with open(f"official_devices/API/changelogs/{codename}.md", "w") as contents:
    contents.write(changelogs)
    contents.write(save)


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
        "last_updated": current_date.strftime("%d %B %Y"),
        "download_link": download_link,
        "archive": f"https://sourceforge.net/projects/pixelos-releases/files/{version_string}/{codename}/",
    }
)

with open(f"API/devices/{codename}.json", "w") as f:
    json.dump(data, f, indent=4)
