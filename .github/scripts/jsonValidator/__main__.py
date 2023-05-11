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


# Device List

headerText = "# Device List\nHere is the list of all the devices actively supprorted officially by PixelOS. To download the latest version of PixelOS, please visit our official website at [PixelOS.net](PixelOS.net), there you can find the necessary resources and information to download and install PixelOS on your device."
footerText = "We hope you enjoyed the project! Your donations help us maintain our infrastructure and continue our work. Please consider showing your support by donating! [Click Me](https://wiki.pixelos.net/docs/donate)"

ReadmeText = headerText + "\n\nNumber Of Devices in Official PixelOS: <**TotalCountGoesHere**>"

officialDeviceList = json.loads(open("API/devices.json", "r").read())

brands = []

for device in officialDeviceList["devices"]:
    if device["vendor"] not in brands and device["active"]:
        brands.append(device["vendor"])

brands = sorted(brands)
brandDevices = {}

totalCount = 0

for brand in brands:
    brandDevices [brand] = []
    for device in officialDeviceList["devices"]:
        if device["vendor"] == brand and device["active"]:
            brandDevices [brand].append(device["model"])
            totalCount += 1
    brandDevices [brand] = sorted(brandDevices [brand])


print (brandDevices)

ReadmeText = ReadmeText + "\n\nNumber of Brands in Official PixelOS: " + str(len(brands))


ReadmeText = ReadmeText + "\n\nOfficially Supported Devices:"

for brand in brands:
    ReadmeText = ReadmeText + "\n\n**" + brand + "**"
    count = 1
    for branddevice in brandDevices[brand]:
        for device in officialDeviceList["devices"]:
            if device["model"] == branddevice:
                ReadmeText = ReadmeText + "\n" + str(count) + ". " + device["model"] + " (" + device["codename_alt"] + ")"
                count +=1


open("docs/DeviceList.md", "w+").write(ReadmeText.replace("<**TotalCountGoesHere**>", str(totalCount)) + "\n\n" + footerText)