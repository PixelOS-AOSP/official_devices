# Keep in mind
This ROM uses EROFS for relevant partitions, due to which:
- Stick to only stock kernel or flash any newer DragonHeart build.
- System is Read-Only (restricts making changes to overlays, system APKs, etc.).
- Avoid using any other recovery than PixelOS recovery which is included.
- You must clean flash if:
    - You are coming from any other ROM or OOS.

# Clean Flash (coming from a different ROM)
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode)
- Flash the recovery by running "fastboot flash recovery <path/to/recovery.img>" in terminal
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to Recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Reboot and voila!

# Dirty Flash / Update
- Download ROM and Recovery to your computer
- Reboot the device to bootloader (Fastboot Mode) [Skip if already using PixelOS recovery]
- Flash the recovery by running "fastboot flash recovery <path/to/recovery.img>" in terminal [Skip if already using PixelOS recovery]
- Reboot to recovery by running "fastboot reboot recovery" in terminal
- On your phone [which is in recovery mode], Apply update > Apply from ADB
- Flash the ROM through ADB sideload by running "adb sideload <path/to/rom.zip>" in terminal
- Reboot and voila!
