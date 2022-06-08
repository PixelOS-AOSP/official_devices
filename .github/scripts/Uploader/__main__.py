#!/usr/bin/env python
#
# Python code which automatically sends a Message in a Telegram Group
# if any new update is found. Intended to be run on every push
#
# Copyright (C) 2021-2022 Ashwin DS <astroashwin@outlook.com>
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

import datetime
import os

SF_PASS = os.environ.get("SF_PASS")

try:
    new_tags = open("new_tags.txt", "r").readlines()
except Exception as e:
    new_tags = []

try:
    OTA = open("no_ota.txt", "r").readlines().replace("\n", "").replace(" ", "") == "no"
except Exception as e:
    OTA = True

cur_dir = os.getcwd()
print(new_tags)
for tag in new_tags:
    os.chdir(cur_dir + "/releases")
    os.system("gh release download " + tag.replace("\n", ""))
    recovery_path = ""
    for file in os.listdir(cur_dir + "/releases"):
        if file == "boot.img":
            os.system("mv " + cur_dir + "/releases/boot.img " + cur_dir + "/releases/boot-" + tag.split("_")[0] + "-" + str(datetime.date.today()).replace("-", "") + ".img")
            break
        if file == "recovery.img":
            os.system("mv " + cur_dir + "/releases/recovery.img " + cur_dir + "/releases/recovery-" + tag.split("_")[0] + "-" + str(datetime.date.today()).replace("-", "") + ".img")
            break
    print("Downloaded")
    os.chdir(cur_dir + "/releases-public")
    os.system("gh release create " + str(datetime.date.today()))
    os.system("gh release upload " + str(datetime.date.today()) + " " + cur_dir + "/releases/*.zip")
    os.system("gh release upload " + str(datetime.date.today()) + " " + cur_dir + "/releases/*.img")
    
    ROM_ZIP_NAME = "none"

    for file in os.listdir(cur_dir + "/releases/"):
        if file.endswith(".zip"):
            ROM_ZIP_NAME = file

    if OTA:
        for file in os.listdir(cur_dir + "/releases/"):
            if file.endswith(".json"):
                device = file.replace(".json", "")
                json = open(cur_dir + "/releases/" + file, "r").read().replace("URL_PLACEHOLDER", "https://sourceforge.net/projects/pixelos-releases/files/twelve/" + device + "/" + ROM_ZIP_NAME)
                open(cur_dir + "/releases/" + file, "w+").write(json)

    else:
        for file in os.listdir(cur_dir + "/releases/"):
            if file.endswith(".json"):
                device = file.replace(".json", "")

    os.system("sudo apt install sshpass")
    # os.system("mkdir ~/.ssh/")
    # os.system("ssh-keyscan frs.sourceforge.net >> ~/.ssh/known_hosts")

    try:
        os.system("sshpass -p " + SF_PASS + " scp -o \"StrictHostKeyChecking no\" " + cur_dir + "/releases/*.img pixelos@frs.sourceforge.net:/home/frs/project/pixelos-releases/twelve/" + device + "/recovery")
        os.system("sshpass -p " + SF_PASS + " scp -o \"StrictHostKeyChecking no\" " + cur_dir + "/releases/*.zip pixelos@frs.sourceforge.net:/home/frs/project/pixelos-releases/twelve/" + device + "")
    except:
        print ("Something went wrong")
    if OTA:
        os.system("cp " + cur_dir + "/releases/*.json " + cur_dir + "/API/updater/" )
    
    print("Uploaded")
    os.system("rm -rf " + cur_dir + "/releases/*.img " + cur_dir + "/releases/*.zip ")
