import json
import os
import pprint


foldersToFormat = [
    "API", "API/devices", "API/updater"
]


def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except Exception as e:
        return False
    return True


def prettyJSON(jsonPath):
    data = json.loads(open(jsonPath).read())
    print(data)
    with open(jsonPath, "w") as write_file:
        json.dump(data, write_file, indent=4)



with open("API/devices.json", "r") as json_file:
    devices = json.load(json_file)

# sort the devices by the "model" field
devices["devices"].sort(key=lambda x: x["model"])

# write the sorted data back to the file
with open("API/devices.json", "w") as json_file:
    json.dump(devices, json_file)

for folder in foldersToFormat:
    for file in os.listdir(folder):
        if file.endswith(".json"):
            print(folder + "/" + file)
            if validateJSON(open(folder + "/" + file).read()):
                print("Json valid")
                prettyJSON(folder + "/" + file)
            else:
                print("json error")
                raise SystemExit("invalid json")
