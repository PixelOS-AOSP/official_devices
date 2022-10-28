# Keep in mind...
- Avoid using ANY other recovery than PixelOS recovery
- Avoid using heavy modes/modules
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI
    - You are coming from A13 September Update or before
- If you fail to follow any of this notes do not blame me for any bugs, you will be ignored

# Clean Flash (coming from a different ROM)
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode)
- Flash the recovery by running "fastboot flash recovery <path/to/recovery.img>" in terminal
- Reboot to recovery by running "fastboot reboot recovery" in terminal OR manually boot to recovery by power button + (Vol+)
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Flash firmware Version (V13.0.1.0 SJGMIXM) through ADB sideload by running "adb sideload <path/to/firmware.zip>" in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu
- Reboot to system and voila!

# Dirty Flash / Update
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode) [Skip if already using PixelOS recovery]
- Flash the recovery by running "fastboot flash recovery <path/to/recovery.img>" in terminal [Skip if already using PixelOS recovery]
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Reboot to system and voila!
