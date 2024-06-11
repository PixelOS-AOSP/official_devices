# Keep in mind...
- DO NOT try to change the included kernel
- DO NOT USE any other recovery than PixelOS recovery which is included.
- You MUST format data with given PixelOS recovery
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI
    - You are coming from previous Android Version

- If you face issues like poor RAM management or storage issues, you have not followed the instructions and/or have changed kernel/recovery. STRICTLY follow the instructions provided again before reporting any issues.
- Formatting with PixelOS Recovery (yes, I mean PixelOS Recovery ONLY) is MUST during clean flash

# Clean Flash (coming from a different ROM)
Clean flash involves formatting data which means you will be loosing data stored in the internal storage of your device, data in SD Card should not be affected. I will not be responsible for any loss of data.
- Download ROM, vendor_boot and boot files to your computer (click on recovery button for vendor_boot and boot)
- Reboot the device to bootloader (Fastboot Mode)
- Flash the vendor_boot by running `fastboot flash vendor_boot <path/to/vendor_boot.img>` in terminal
- Flash the boot by running `fastboot flash boot <path/to/boot.img>` in terminal
- Reboot to recovery by running `fastboot reboot recovery` in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to Recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Flash firmware (Version OS1.0.2.0.TKHMIXM) through ADB sideload by running `adb sideload <path/to/firmware.zip>` in terminal
- Reboot and voila!

# Dirty Flash / Update
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM file to your computer
- Reboot the device to recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Flash firmware (Version OS1.0.2.0.TKHMIXM) through ADB sideload by running `adb sideload <path/to/fw.zip>` in terminal
- Reboot and voila!
