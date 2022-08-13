# Keep in mind...
This ROM comes with EROFS formatting, due to which:
- Avoid Changing Kernel (unless it supports EROFS)
- System is Read-Only (restricts making changes to overlays, system APKs, etc.)
- Avoid using any other recovery than PixelOS recovery which is included (If you wish to use, check for EROFS compatibility)
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI
    - You are coming from July 2022 Update or before

# Clean Flash (coming from a different ROM)
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode)
- Flash the recovery by running "fastboot flash boot <path/to/recovery.img>" in terminal
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to Recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Flash firmware (Version V13.0.9.0SKGMIXM) through ADB sideload by running "adb sideload <path/to/firmware.zip>" in terminal
- Reboot and voila!

# Dirty Flash / Update
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode) [Skip if already using PixelOS recovery]
- Flash the recovery by running "fastboot flash boot <path/to/recovery.img>" in terminal [Skip if already using PixelOS recovery]
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Flash firmware (Version V13.0.9.0SKGMIXM) through ADB sideload by running "adb sideload <path/to/fw.zip>" in terminal
- Reboot and voila!
