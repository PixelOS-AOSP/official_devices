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
try:
    new_tags = open("new_tags.txt", "r").readlines()
except Exception as e:
    new_tags = []

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
    print("Uploaded")
    os.system("rm -rf " + cur_dir + "/releases/*.img " + cur_dir + "/releases/*.zip ")
