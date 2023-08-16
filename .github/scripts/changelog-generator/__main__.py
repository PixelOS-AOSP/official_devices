#!/usr/bin/env python
#
# Copyright (C) 2021-2023 Ashwin DS <astroashwin@outlook.com> and PixelOS <admin@PixelOS.net>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation;
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import requests
import os
import json
import time
from datetime import datetime


auth = os.environ.get("GH_PAT")
org = "PixelOS-AOSP"
last_updated = open(".github/scripts/changelog-generator/last_updated.txt", "r").read().split("\n")[0].replace(" ", "")

auth_json = {
    "Authorization": "Bearer " + auth,
}

ignoreList = ["official_devices", "wiki", "OTA-Devices"]

raw_members = requests.get("https://api.github.com/orgs/" + org + "/members", headers=auth_json).json()
members = []
for member in raw_members:
    members.append(member["login"])
    member_info = requests.get("https://api.github.com/users/" + member["login"], headers=auth_json).json()
    if member_info != None and member_info["name"] != None and member_info["name"] != "None" :
        members.append(member_info["name"])


def get_full_date():
    with open('.github/scripts/changelog-generator/last_updated.txt', 'r') as file:
        date_string = file.readline().strip()

    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    full_date = date_object.strftime("%d %B %Y")

    return full_date


def mkdn_links(text, url):
    return f"[{text}]({url})"


def getCommits(repo_name):
    # YYYY-MM-DDTHH:MM:SSZ
    commits = requests.get("https://api.github.com/repos/" + repo_name + "/commits?since=" + last_updated, headers=auth_json).json()
    commitNumber = 0
    changes = ""
    for commit in commits:
        if (commit["committer"] != None and commit["committer"]["login"] in members) or (commit["commit"]["committer"]["name"] in members):
            commitNumber += 1
            changes = changes + "- " + mkdn_links( commit["commit"]["message"].split("\n")[0] + " (" + commit["commit"]["committer"]["date"].split("T")[0] +") ", commit["html_url"]) + "\n"

    if commitNumber > 0:
        changes = "## " + repo_name.split("/")[1] + "\n" + changes
        return changes

    else:
        return ""


raw_repo_list = requests.get("https://api.github.com/orgs/" + org + "/repos" , headers=auth_json).json()

ChangeLog = ""
for repo in raw_repo_list:
    if repo["full_name"].split("/")[1] in ignoreList:
        continue
    else:
        print (repo["full_name"])
        time.sleep(1)
        Changes = getCommits (repo["full_name"])
        if Changes != "":
            ChangeLog = ChangeLog + Changes + "\n\n"


ChangeLog = "# Changes since " + get_full_date() + "\n\n" + ChangeLog 

print (ChangeLog)    

existing = open("API/changelogs/source.md", "r").read()
open("API/changelogs/source.md", "w+").write(ChangeLog + "\n\n" + existing)

formatted_datetime = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

open(".github/scripts/changelog-generator/last_updated.txt", "w+").write(formatted_datetime)