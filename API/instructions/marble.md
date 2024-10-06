# Clean Flash (coming from a different ROM)
- Download ROM, boot, vendor_boot, dtbo and recovery files to your computer (click on recovery button for downloading)
- Reboot the device to bootloader (Fastboot Mode)
- Flash boot by running `fastboot flash boot <path/to/boot.img>` in terminal
- Flash vendor_boot by running `fastboot flash vendor_boot <path/to/vendor_boot.img>` in terminal
- Flash dtbo by running `fastboot flash dtbo <path/to/dtbo.img>` in terminal
- Flash recovery by running `fastboot flash recovery <path/to/recovery.img>` in terminal
- Reboot to recovery by running `fastboot reboot recovery` in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to Recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Reboot and voila!

# Dirty Flash / Update
- Download ROM file to your computer
- Reboot the device to recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Reboot and voila!
