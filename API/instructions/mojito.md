# Keep in mind...
- DO NOT try to change the included kernel
- System is Read-Only (restricts making changes to overlays, system APKs, etc.)
- DO NOT USE any other recovery than PixelOS recovery which is included.
- You MUST format data with given PixelOS recovery
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI
    - You are coming from previous Android Version

- If you face issues like poor RAM management or storage issues, you have not followed the instructions and/or have changed kernel/recovery. STRICTLY follow the instructions provided again before reporting any issues.
- Formatting with PixelOS Recovery (yes, I mean PixelOS Recovery ONLY) is MUST during clean flash

# Clean Flash (coming from a different ROM)
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode)
- Flash the recovery by running "fastboot flash vendor_boot <path/to/vendor_boot.img>" in terminal
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to Recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Flash firmware (Version V13.0.11.0.SKGMIXM) through ADB sideload by running "adb sideload <path/to/firmware.zip>" in terminal
- Reboot and voila!

# Dirty Flash / Update
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode) [Skip if already using PixelOS recovery]
- Flash the recovery by running "fastboot flash vendor_boot <path/to/vendor_boot.img>" in terminal [Skip if already using PixelOS recovery]
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Flash firmware (Version V13.0.11.0.SKGMIXM) through ADB sideload by running "adb sideload <path/to/fw.zip>" in terminal
- Reboot and voila!
