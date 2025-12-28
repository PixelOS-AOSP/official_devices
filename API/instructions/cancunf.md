## Introduction

Before we begin, let me make it perfectly clear that,

```
Your warranty is now void.

I am not responsible for bricked devices, dead SD cards, thermonuclear war, or you getting fired because the alarm app failed.
Please do some research if you have any concerns about features included in this ROM before flashing it!
YOU are choosing to make these modifications, and if you point the finger at me for messing up your device, I will laugh at you.
```

as well as the fact that this guide is only meant to be followed for **Android 16 ROMs (and newer) which are based off of Android 15 Firmware.**

Also to add: This guide is ONLY for devices that are codenamed cancunf (G64 is cancunf as well) and that you need a PC to do this.

Be warned that if you are already progressing with an update on Stock, you must complete the update, reboot to system and then follow the instructions to unlock the bootloader and flash ROMs.

## Unlocking the Bootloader

### Setting up the environment

First and foremost, install the [Google USB Drivers (Windows)](https://dl.google.com/android/repository/usb_driver_r13-windows.zip) on your PC by extracting the zip and right-clicking on the `android_winusb.inf` file then clicking install. You can skip this step if you are on Linux or macOS.

Next, download and extract the Platform Tools required to unlock the bootloader and flash ROMs. You can get them from the links below:

[Platform Tools (Windows)](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)

[Platform Tools (macOS)](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip)

[Platform Tools (Linux)](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)

### Enabling OEM Unlocking toggle

Moving on, you need to enable OEM Unlocking toggle from the Developer Options page.

If the phone is new, you would have to wait for 7 days before you can enable that toggle as it will be greyed out.

To enable the Developer Options page, you would need to go to About Phone -> Device Identifiers and Tap on the Build number for 7 times in the Settings app.

### Getting Device ID

Then, you would need to get your **Device ID** to generate the Unlock Token.

You do that by opening a Terminal / Command Prompt / PowerShell Terminal in the folder/directory where the Platform Tools are extracted.

Then, turn off your device, push and hold the power and volume down button at the same time and release once the phone has booted into the Bootloader Mode.

Run ```fastboot devices``` to see if the device is detected.

An example output would be as such:

```
ZY22HZLCR2	fastboot
```

If you have installed the USB drivers properly, it will show that the device is connected.

Run, ```fastboot oem get_unlock_data``` to get the Device ID.

e.g:

```
(bootloader) Unlock data:
(bootloader) 0A40040192024205#4C4D3556313230
(bootloader) 30373731363031303332323239#BD00
(bootloader) 8A672BA4746C2CE02328A2AC0C39F95
(bootloader) 1A3E5#1F53280002000000000000000
(bootloader) 0000000
```

### Getting Unlock Token

To generate the unlock token, you'll need to merge the 5 lines of output into one string without any extra spaces or additional text. An example of that would be:

```
0A40040192024205#4C4D355631323030373731363031303332323239#BD008A672BA4746C2CE02328A2AC0C39F951A3E5#1F532800020000000000000000000000
```

Then, go to the [Motorola Unlock Website](https://en-us.support.motorola.com/app/standalone/bootloader/unlock-your-device-b). Login to your account and paste the **Device ID** string and click on **Can my device be unlocked?** to check eligibility for unlock, then accept the legal agreement and click on **Request Unlock key**.

You will then receive an email with your Unlock Token. Check your spam folder if you had not received it. Within the email would contain a unique 20-character, alphanumeric code that you will use to unlock your device.

### Unlock process

Type ```fastboot oem unlock ``` and paste your unique 20-character, alphanumeric code that you have received via email and run it.

e.g: 

```
fastboot oem unlock MZMC6D342TBNNWI6TRP9
```

If you have run the command correctly, your device's screen will confirm that your device is unlocked.

**Congratulations**, you have just successfully unlocked the bootloader of your device, moving forward when you reboot, it will show a warning screen that your **Bootloader has been unlocked**.

## Flashing ROMs

### Download the relevant files

Now that you have unlocked the bootloader, download the following files from the ROM posts:

- ROM zip.
- Initial install zip.

e.g: PixelOS_cancunf-16.0-20251111-0513.zip and PixelOS\_16\_cancunf\_initial\_install.zip

The initial install zip has the boot and vendor\_boot images bundled together.

**You don’t need to \`fill your slots\` or \`flash Android 15 stock\` beforehand, as the ROMs already bundle Android 15 firmware, unless your device is on anything older than Android 14 May 2024 stock (U1TDS34.94-12-7-5), in which case you’ll need to re-flash the same ROM (without formatting data) to ensure both slots have post-ARB firmware.**

### Flash the initial install zip

Turn off your device, push and hold the power and volume down button at the same time and release once the phone has booted into the Bootloader Mode.

Open a Terminal / Command Prompt / PowerShell Terminal and run ```fastboot reboot fastboot```.

Once the phone has booted into the FastbootD Mode, run ```fastboot devices``` to see if the device is detected.

An example output would be as such:

```
ZY22HZLCR2	fastbootd
```

Remember, it has to say fastbootd, not fastboot. If it says fastboot, re-read the instructions again.

The reason why you need to be in fastbootd and not bootloader (fastboot) is because you cannot flash images in bootloader due to Motorola implementing a sort of timestamp check within the bootloader which then results in an error like such:

```
Writing 'boot_b'                                   (bootloader) Preflash validation failed
FAILED (remote: '')
fastboot: error: Command failed
```

As such, you NEED to be in fastbootd to flash the initial install zip.

If it is not detected, you should re-read Unlocking the Bootloader part as to installing the relevant USB drivers.

Moving on, type ```fastboot --skip-reboot update ``` and then drag-and-drop the initial install zip into the terminal and run it.

e.g:

```
fastboot --skip-reboot update PixelOS_16_cancunf_initial_install.zip
```

### Format Data

Once it has flashed without any errors, you may proceed by running ```fastboot reboot recovery```.

Then you can choose the **Wipe data / Factory reset** option on your device to format the /data partition.

### Flash ROMs

Finally, choose the **Apply update from ADB / Apply update -> Apply update from ADB / Install update -> ADB Sideload** option on your device and then type ```adb sideload ``` in the Terminal and then drag-and-drop the ROM zip into the terminal and run it.

e.g:

```
adb sideload PixelOS_cancunf-16.0-20251111-0513.zip
```

Once the process has been completed without any errors, proceed to reboot your device into your newly flashed ROM :)

### Updating to a newer build

To update to a newer build, you start by downloading the ROM zip and then you have two options:

#### Flashing via the built-in Updater

To flash via the built-in Updater:

On ROMs that are in an Official status, they typically provide OTA updates. So, you can just go to the Updater and click Flash.

On ROMs that are not in an Official status but provide an Updater that has a **Local Update** option, you can download the ROM zip in your phone and click **Local Update** then choose the downloaded file to start the update process.

Once you have done either one of those things, you can reboot to boot into your newly updated ROM :)

#### Sideloading in recovery

To sideload in recovery, first you turn off your device, push and hold the power and volume down button at the same time and release once the phone has booted into the Bootloader Mode.

Open a Terminal / Command Prompt / PowerShell Terminal and run ```fastboot reboot recovery```.

Then, choose the **Apply update from ADB / Apply update -> Apply update from ADB / Install update -> ADB Sideload** option on your device and then type ```adb sideload ``` in the Terminal and then drag-and-drop the ROM zip into the terminal and run it.

Once the process has been completed without any errors, proceed to reboot your device into your newly updated ROM :)
