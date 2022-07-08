import json
import os
import pprint


foldersToFormat = [
    "API", "API/devices"
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
