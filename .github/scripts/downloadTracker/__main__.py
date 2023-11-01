import requests
import re
import os
import json
from datetime import date

ORG="pixelos-releases"
REPO_NAME="releases-public"
DIR_PATH="API/downloads"

API_ENDPOINT = f"https://api.github.com/repos/{ORG}/{REPO_NAME}/releases"

def add_dictionary_values(dict1:dict, dict2:dict) -> dict:
    new_dict = dict1.copy()
    for key,value in dict2.items():
        if key in new_dict:
            new_dict[key] += value
        else:
            new_dict[key] = value
    return new_dict

def fetch_new_downloads() -> dict:
    # empty new json
    new_json = {}
    
    # get the API repsonse
    all_releases = requests.get(API_ENDPOINT).json()
    
    # filter through all filenames
    for tags in all_releases:
        tag_data = []
        for asset in tags['assets']:
            file_name = asset['name']

            # match the filename to a given regex, group 0 here is devicename
            rom_name = re.match("^PixelOS_(.+?)-.+?\.zip$",file_name)

            # if regex matches, get the device name, associate it with its download count
            if rom_name: 
                tag_data.append({rom_name.groups()[0] : asset['download_count']})

        # add the tag entry with all device and download count
        new_json[tags['tag_name']] = tag_data

    return new_json

def merge_download_count(data:dict):
    final = 0
    for _, value in data.items():
        for items in value:
            final += sum(items.values())
    return final

def sf_download_count(path: str = None):
    SF_URL = f"https://sourceforge.net/projects/{ORG}/files/"
    if path is not None: SF_URL += path.strip('/')
    SF_URL += f"/stats/json?start_date=2022-01-15&end_date={date.today().strftime('%Y-%m-%d')}"
    resp = requests.get(SF_URL)
    if resp.ok : return resp.json()['total']
    # return NONE on error, many devices non-existent on sf

def sf_per_device_count(device_list : list[str]) -> dict:
    _sf_json = {}
    android_versions = ["fourteen", "thirteen", "twelve"]
    for android in android_versions:
        _android_tmp = {}
        for device in device_list:
            count = sf_download_count(f"{android}/{device}")
            if count is not None:
                _android_tmp[device] = count

        _sf_json = add_dictionary_values(_sf_json,_android_tmp)

    return _sf_json

def gh_per_device_count(gh_data:dict) -> dict:
    _gh_json = {}
    for _,value in gh_data.items():
        for d_pair in value:
            _gh_json = add_dictionary_values(_gh_json,d_pair)
    return _gh_json

if __name__ == '__main__':
    # load the old json as python dict
    with open(f"{DIR_PATH}/per_tag.json","r") as fp:
        old_json = json.load(fp)

    # fetch new data from github
    new_json = fetch_new_downloads()

    # update the old json with new values
    latest_json = {**old_json, **new_json}

    # dump the updated json
    with open(f"{DIR_PATH}/per_tag.json","w") as fp:
        json.dump(latest_json,fp, indent=4)

    with open(f"{DIR_PATH}/total.json","w") as fp:
        ghdc = merge_download_count(latest_json)
        sfdc = sf_download_count()
        data = {
                "github":ghdc,
                "sourceforge":sfdc,
                "total": (ghdc+sfdc)                
                }
        json.dump(data, fp, indent=4)

    # per device, github and sf combined
    with open(f"{DIR_PATH}/per_device.json","w") as fp:
        # get device names from API folder
        device_list = [ i.replace('.json','') for i in os.listdir('API/devices') if i.endswith('.json') ]
        _sf_per_device = sf_per_device_count(device_list)
        _gh_per_device = gh_per_device_count(latest_json)
        json.dump(add_dictionary_values(_sf_per_device,_gh_per_device),fp,indent=4)
