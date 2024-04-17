# Keep in mind...
- DO NOT USE any other recovery than PixelOS recovery which is included
- HyperOS Global firmware included (OS1.0.3.0.ULFMIXM)
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI

# Clean Flash (coming from a different ROM)
Clean flash involves formatting data which means you will loose your data that is stored in the internal storage of your device. I will not be responsible for any loss of data!
- Download ROM, boot, vendor_boot, dtbo and recovery images (click on recovery button for the files)
- Reboot the device to bootloader (Fastboot Mode)
- Flash the boot by running `fastboot flash boot <path/to/boot.img>` in terminal
- Flash the vendor_boot by running `fastboot flash vendor_boot <path/to/vendor_boot.img>` in terminal
- Flash the dtbo by running `fastboot flash dtbo <path/to/dtbo.img>` in terminal
- Flash the recovery by running `fastboot flash dtbo <path/to/recovery.img>` in terminal
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
