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
BOT_API = os.environ.get("BOT_API")  # Telegram Bot API Token
# GitHub PAT (for accessing private repos and APIs)
TOKEN = os.environ.get("TOKEN")
android_Version_text = "fourteen"
GITHUB_API_USER = "geek0609"  # GitHub username of owner of the above token
# ID of channel where it needs to post [Requires admin with enough permissions]
CHAT_ID = "-1001551285228"
# Direct link to banner
banner = "https://raw.githubusercontent.com/PixelOS-Releases/banners/" + android_Version_text + "/pixelos.JPEG"
json_dir = "./API/devices/"  # Directory where it should look for JSONs
timeout = 1  # Time out before sending consecutive messages
LOG_DIR = ".github/scripts/UpdatePoster/log.txt"
WEBSITE_DOWNLOAD = "https://pixelos.net/download/"
# Tags which needs to appear at end of the post
FOOTER_TAGS = "#TeamPixel #PixelOS"

# UniqueID can be any parameter contained in the device.json file which is unique to one build which the\
# maintainer must change every update/build.
# So, to update, maintainer must eventually change that and when its changed, the program can compare the
# older list to latest and find out what device is changed, so that is the device which got an update and
# needs to be posted then now since we know what device got update, take its info from API, and use it to post
UniqueID = "private_download_tag"

# Inititalize the bot
bot = Bot(BOT_API)
updater = Updater(BOT_API, use_context=True, workers=1)
dispatcher = updater.dispatcher


def get_Device_banner (device):
    return banner
    DeviceBanner = "https://raw.githubusercontent.com/PixelOS-Releases/banners/" + android_Version_text + "/" + device + ".jpg"
    if (requests.get(DeviceBanner).status_code == 200):
        return DeviceBanner
    else:
        return banner
 

# HTML Hyperlink Fomatting
def html_link(url, text):
    return "<a href=\"" + url + "\">" + text + "</a>"


# HTML Bold Fomatting
def html_bold(text):
    return "<b>" + text + "</b>"


# HTML monospace/code Fomatting
def html_code(text):
    return "<code>" + text + "</code>"


def send_message(message: str):
    bot.send_message(chat_id=CHAT_ID, tex=message,
                     disable_web_page_preview=True)


def send_photo(message: str, picture):
    bot.send_photo(chat_id=CHAT_ID, caption=message,
                   photo=picture, parse_mode="html")


# returns list of new tags
def get_updated_tags():
    tags = []
    for file in os.listdir(json_dir):
        if file != "README.MD" and json.loads(open(json_dir + file, "r").read())[UniqueID] != "":
            tags.append(json.loads(
                open(json_dir + file, "r").read())[UniqueID])
    return tags


# returns tags which are currently logged
def get_current_tags():
    tags = []
    for tag in open(LOG_DIR).readlines():
        tags.append(tag.replace("\n", ""))
    return tags


# returns list of devices which are updated
def get_updated_device():
    devices_changed = []
    for new in list(set(get_updated_tags()) - set(get_current_tags())):
        for file in os.listdir(json_dir):
            if file != "README.MD":
                if json.loads(open(json_dir + file, "r").read())[UniqueID] == new:
                    devices_changed.append(file.replace(".json", ""))
    return devices_changed


# To make the post
def post_maker(device_info, name):
    message = "<b>PixelOS for " + device_info["device_display_name"] + " (" + \
              device_info["device_display_codename"] + \
        ")\n\nVersion:</b> " + device_info["version"]

    if device_info["beta"]:
        message = message + " (beta)\n"
    else:
        message = message + "\n"

    message = message + "<b>Maintainer:</b> "

    loop = len(device_info["maintainer"])
    for maintainer in device_info["maintainer"]:

        if loop == 1 & loop != len(device_info["maintainer"]):
            message = message + " & "
        elif loop != len(device_info["maintainer"]):
            message = message + ", "

        message = message + "<a href=\"" + \
            maintainer["telegram"] + "\">" + \
            maintainer["display_name"] + "</a>"

        loop -= 1

    release_info = json.loads(requests.get(
        "https://api.github.com/repos/PixelOS-Releases/releases/releases/tags/" +
        device_info[UniqueID],
        auth=(GITHUB_API_USER, TOKEN)).content)  # information about the release, taken from Private Releases Repository

    recovery_file_size = 0
    rom_file_size = 0
    upload_date = str(datetime.date.today())

    # Fallback values
    ROM_NAME = ""
    RECOVERY_NAME = "error"

    for asset in release_info["assets"]:
        if asset["name"] == "boot.img" or asset["name"] == "recovery.img":
            recovery_file_size = float(asset["size"]) * 0.00000095367432
            RECOVERY_NAME = asset["name"]
        elif asset["name"].__contains__("PixelOS.part"):
            rom_file_size = rom_file_size + float(asset["size"]) * 0.00000000093132
        elif asset["name"].endswith(".zip"):
            ROM_NAME = asset["name"]
            rom_file_size = float(asset["size"]) * 0.00000000093132
            upload_date = asset["created_at"]

    message = message + "\n<b>Upload Date:</b> " + \
        upload_date[0:10].split("-")[-1] + "-" \
        + ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov",
           "Dec"][int(upload_date[0:10].split("-")[-2]) - 1] + "-" + upload_date[0:10].split("-")[-3]

    message = message + "\n\n<b>Download:</b> <a href=\"" + WEBSITE_DOWNLOAD + name + "\">Website</a>\n"

    # Download Sizes
    message = message + "<b>Size:</b> " + str(rom_file_size)[0:4] + "G (ROM)\n"

    if device_info["xda"] != None and device_info["xda"] != "":
        message = message + "<b><a href=\"" + \
            device_info["xda"] + "\">XDA Thread</a></b> (FAQ)\n"

    message = message + "\n"  # Leave a line unconditionally

    if not device_info["updater"]:
        message = message + "<b>⚠️Clean flash mandatory</b>\n\n"
    else:
        open("no_ota.txt", "w+").write("no")

    for codename in device_info["device_display_codename"].split("/"):
        message = message + "#" + codename + " "

    if device_info["beta"]:
        message = message + "#beta "

    return message + FOOTER_TAGS


# updates the log file
def update():
    open(LOG_DIR, "w+").write("")
    for tag in get_updated_tags():
        open(LOG_DIR, "a").write(tag + "\n")


# grabs info of what files needs to be uplaoded for release
def uploader():
    open("new_tags.txt", "w+").write("")
    for tag in list(set(get_updated_tags()) - set(get_current_tags())):
        open("new_tags.txt", "a").write(tag + "\n")


for device in get_updated_device():
    banner = get_Device_banner(device)
    current_device_info = json.loads(open(json_dir + device + ".json").read())
    # print(post_maker(current_device_info))
    send_photo(post_maker(current_device_info, device),
               requests.get(banner).content)
    time.sleep(timeout)

if len(get_updated_device()) != 0:
    uploader()
    update()
