# Clean Flash (coming from a different ROM)
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode)
- Flash the recovery by running "fastboot flash boot <path/to/recovery.img>" in terminal
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Flash firmware (Version V13.0.5.0.SKGMIXM) through ADB sideload by running "adb sideload <path/to/fw.zip>" in terminal
- Once it finishes installing, go back to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to system
- Reboot and voila!

# Dirty Flash / Update
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode) [Skip if already using PixelOS recovery]
- Flash the recovery by running "fastboot flash boot <path/to/recovery.img>" in terminal [Skip if already using PixelOS recovery]
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Flash firmware (Version V13.0.5.0.SKGMIXM) through ADB sideload by running "adb sideload <path/to/fw.zip>" in terminal
- Reboot and voila!
