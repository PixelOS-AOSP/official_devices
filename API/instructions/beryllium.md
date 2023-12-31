# Keep in mind...
- DO NOT try to change the included kernel
- DO NOT USE any other recovery than PixelOS recovery which is included.
- You MUST format data with given PixelOS recovery
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI
    - You are coming from previous Android Version
    - You are coming from Non Retrofit ROM

- If you face issues like poor RAM management or storage issues, you have not followed the instructions and/or have changed kernel/recovery. STRICTLY follow the instructions provided again before reporting any issues.
- Formatting with PixelOS Recovery (yes, I mean PixelOS Recovery ONLY) is MUST during clean flash

# Clean Flash (coming from a different ROM)
Clean flash involves formatting data which means you will be loosing data stored in the internal storage of your device, data in SD Card should not be affected. I will not be responsible for any loss of data.
- Download ROM, recovery and super_empty files to your computer (click on recovery button for recovery and super_empty)
- Reboot the device to bootloader (Fastboot Mode)
- Flash empty super image by running `fastboot wipe-super <path/to/super_empty.img>` in terminal
- Flash recovery image by running `fastboot flash recovery <path/to/recovery.img>` in terminal
- Reboot to recovery mode
- Go to main menu > Factory reset > Format data/factory reset >  Format data - Back to Main menu
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Reboot and voila!

# Dirty Flash / Update
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM file to your computer
- Reboot the device to recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Reboot and voila!

# Notes
- If you get the following error: fastboot: usage: unknown command wipe-super, make sure ADB and fastboot are updated to the latest version. You need fastboot version 28.0.2 or greater.
- If installation fails with the following error: [liblp]Logical partition metadata has invalid geometry magic signature., make sure you did the previous step properly, and repeat it if needed
