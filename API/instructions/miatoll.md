# Keep in mind ...
- DO NOT USE any other recovery than the recommended TWRP or PixelOS recovery which is included
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI
    - You are coming from previous Android Version

# Clean flash (coming from a different ROM):
Clean flash involves formatting data which means you will be loosing data stored in the internal storage of your device, data in SD Card should not be affected. I will not be responsible for any loss of data.
- Download ROM, TWRP recovery (click [HERE](https://t.me/clarencebuilds/116) for TWRP) and your device specific firmware (click [HERE](https://xiaomifirmwareupdater.com/)) to your computer
- Reboot the device to bootloader (Fastboot Mode)
- Flash the recovery by running `fastboot flash recovery <path/to/recovery.img>` in terminal
- Reboot to recovery by running `fastboot reboot recovery` in terminal
- Go to Advanced > Enable ADB Sideload
- (Optional) Flash the firmware through ADB sideload by running `adb sideload <path/to/firmware.zip>`
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Go to main menu > Wipe > Format Data > Type "yes" and confirm
- Reboot to system

# Dirty Flash / Update
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM file to your computer
- Reboot the device to recovery
- On your phone [which is in recovery mode], go to Advanced > Enable ADB Sideload
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
