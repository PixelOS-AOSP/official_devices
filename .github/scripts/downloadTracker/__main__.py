from urllib.request import urlopen
import re
import json
from datetime import date

ORG="pixelos-releases"
REPO_NAME="releases-public"
DIR_PATH="API/downloads"

API_ENDPOINT = f"https://api.github.com/repos/{ORG}/{REPO_NAME}/releases"

def fetch_new_downloads() -> dict:
    # empty new json
    new_json = {}
    
    # get the API repsonse
    resp = urlopen(API_ENDPOINT)
    encoding = resp.info().get_content_charset('utf-8')
    all_releases = json.loads(resp.read().decode(encoding))
    
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

def sf_download_count():
    SF_URL = f"https://sourceforge.net/projects/{ORG}/files/stats/json?start_date=2022-01-15&end_date={date.today().strftime('%Y-%m-%d')}"
    resp = urlopen(SF_URL)
    encoding = resp.info().get_content_charset('utf-8')
    json_resp = json.loads(resp.read().decode(encoding))

    return json_resp['total']

if __name__ == '__main__':
    # load the old json as python dict
    with open(f"{DIR_PATH}/per_tag.json","r") as fp:
        old_json = json.load(fp)

    # fetch new data from github
    new_json = fetch_new_downloads()

    # update the old json with new values
    old_json.update(new_json)

    # dump the updated json
    with open(f"{DIR_PATH}/per_tag.json","w") as fp:
        json.dump(old_json,fp, indent=4)

    with open(f"{DIR_PATH}/total.json","w") as fp:
        ghdc = merge_download_count(old_json)
        sfdc = sf_download_count()
        data = {
                "github":ghdc,
                "sourceforge":sfdc,
                "total": (ghdc+sfdc)                
                }
        json.dump(data, fp, indent=4)
