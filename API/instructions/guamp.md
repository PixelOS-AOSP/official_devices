# Keep in mind...
- WARNING: If you are flashing Custom ROM for first time, you should install `copy-partition.zip`
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or Stock ROM
    - You are coming from previous Android Version

# Clean Flash (coming from a different ROM) - Recommended
Clean flash involves formatting data which means you will loose your data that is stored in the internal storage of your device. I will not be responsible for any loss of data!
- Download ROM, and Recovery (Lastest TWRP or PixelOS Recovery)
- Reboot the device to bootloader
- Flash the recovery by running `fastboot flash recovery <path/to/recovery.img>` in terminal
- Reboot to recovery by running `fastboot reboot recovery` in terminal
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to Recovery
- Reboot and voila!

# Dirty Flash / Update
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM file to your computer
- Reboot the device to recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Reboot and voila!
