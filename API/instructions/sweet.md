# Keep in mind...
This ROM comes with EROFS formatting, due to which:
- Do NOT change kernel
- System is Read-Only (restricts making changes to overlays, system APKs, etc. directly, however you can replace stuff with Magisk)
- Avoid using any other recovery than PixelOS recovery
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI
    - You are coming from previous Android Version

# Clean flash (coming from a different ROM):
Clean flash involves formatting data which means you will be loosing data stored in the internal storage of your device, data in SD Card should not be affected. I will not be responsible for any loss of data.
- Download ROM and recovery files to your computer
- Reboot the device to bootloader (Fastboot Mode)
- Flash the recovery by running `fastboot flash recovery <path/to/recovery.img>` in terminal
- Reboot to recovery by holding volume up + power button
- Go to Advanced > Enable ADB Sideload
- Flash the latest MIUI 14 firmware for your region through ADB sideload by running `adb sideload <path/to/firmware.zip>`
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Go to main menu > Wipe > Format Data > Type "yes" and confirm
- Reboot and voila!

# Dirty Flash / Update
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM file to your computer
- Reboot the device to recovery
- On your phone [which is in recovery mode], go to Advanced > Enable ADB Sideload
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Reboot and voila!