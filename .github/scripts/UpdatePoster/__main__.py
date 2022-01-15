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

import sys
import datetime
import json
import os
import time

import requests
from telegram import *
from telegram.ext import *

# Get Secrets from Workflow
BOT_API = os.environ.get("BOT_API")
CHAT_ID = "-1001551285228"
bot = Bot(BOT_API)
TOKEN = os.environ.get("TOKEN")
updater = Updater(BOT_API, use_context=True, workers=1)
dispatcher = updater.dispatcher
banner = "https://raw.githubusercontent.com/PixelOS-Devices/stuff/main/banner/PixelOS-15-Jan-2022.png"
json_dir = "./API/devices/"
timeout = 10


def send_message(message: str):
    bot.send_message(chat_id=CHAT_ID, tex=message, disable_web_page_preview=True)


def send_photo(message: str, picture):
    bot.send_photo(chat_id=CHAT_ID, caption=message, photo=picture, parse_mode="html")


def get_updated_tags():
    tags = []
    for file in os.listdir(json_dir):
        if file != "README.MD" and json.loads(open(json_dir + file, "r").read())["private_download_tag"] != "":
            tags.append(json.loads(open(json_dir + file, "r").read())["private_download_tag"])
    return tags


def get_current_tags():
    tags = []
    for tag in open(".github/scripts/UpdatePoster/log.txt").readlines():
        tags.append(tag.replace("\n", ""))
    return tags


def get_updated_device():
    devices_changed = []
    for new in list(set(get_updated_tags()) - set(get_current_tags())):
        for file in os.listdir(json_dir):
            if file != "README.MD":
                if json.loads(open(json_dir + file, "r").read())["private_download_tag"] == new:
                    devices_changed.append(file.replace(".json", ""))

    return devices_changed


def post_maker(device_info):
    message = "<b>PixelOS for " + device_info["device_display_name"] + " (" + \
              device_info["device_display_codename"] + ")\n\nVersion:</b> " + device_info["version"]

    if device_info["beta"]:
        message = message + " beta\n"
    else:
        message = message + "\n"

    message = message + "<b>Maintainer:</b> "

    loop = len(device_info["maintainer"])
    for maintainer in device_info["maintainer"]:

        if loop == 1 & loop != len(device_info["maintainer"]):
            message = message + " & "
        elif loop != len(device_info["maintainer"]):
            message = message + ", "

        message = message + "<a href=\"" + maintainer["telegram"] + "\">" + maintainer["display_name"] + "</a>"

        loop -= 1

    release_info = json.loads(requests.get(
        "https://api.github.com/repos/PixelOS-Releases/releases/releases/tags/" + device_info["private_download_tag"],
        auth=("geek0609", TOKEN)).content)

    recovery_file_size = 0
    rom_file_size = 0
    upload_date = datetime.date.today()

    for asset in release_info["assets"]:
        if asset["name"] == "boot.img" or asset["name"] == "recovery.img":
            recovery_file_size = float(asset["size"]) * 0.00000095367432
        else:
            rom_file_size = float(asset["size"]) * 0.00000000093132
            upload_date = asset["created_at"]

    message = message + "\n<b>Upload Date:</b> " + \
              upload_date[0:10].split("-")[-1] + "-" \
              + ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov",
                 "Dec"][int(upload_date[0:10].split("-")[-2]) - 1] + "-" + upload_date[0:10].split("-")[-3]

    message = message + "\n\n<b>Download:</b> <a href=\"" + device_info["public_download"] + "\">ROM | Recovery</a>\n" \
              "<b>Size:</b> " + str(rom_file_size)[0:4] + "G (ROM) | " + str(int(recovery_file_size)) + "M (Recovery)\n\n"

    for codename in  device_info["device_display_codename"].split("/"):
        message = message + "#" + codename + " "

    if device_info["beta"]:
        message = message + "#beta "

    return message + "#TeamPixel #PixelOS"


def update():
    open(".github/scripts/UpdatePoster/log.txt", "w+").write("")
    for tag in get_updated_tags():
        open(".github/scripts/UpdatePoster/log.txt", "a").write(tag + "\n")


def uploader():
    open("new_tags.txt", "w+").write("")
    for tag in list(set(get_updated_tags()) - set(get_current_tags())):
        open("new_tags.txt", "a").write(tag + "\n")


for device in get_updated_device():
    current_device_info = json.loads(open("API/devices/" + device + ".json").read())
    # print(post_maker(current_device_info))
    send_photo(post_maker(current_device_info),
               requests.get("https://raw.githubusercontent.com/PixelOS-Devices/stuff/main/PixelOS-Shenhe.png").content)
    # time.sleep(timeout)

if len(get_updated_device()) != 0:
    uploader()

update()
