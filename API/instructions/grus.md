# Keep in mind:
- Use PixelOS Recovery only

# Clean flash (coming from a different ROM):
- Make sure your device's bootloader is unlocked
- Reboot to bootloader mode (Fastboot)
- Download the recovery image for your device (present in PixelOS SourceForge)
- Flash the recovery by running `fastboot flash recovery <path/to/recovery.img>` in terminal
- Reboot to recovery by holding volume up + power button
- Go to Advanced > Enable ADB Sideload
- Download ROM and firmware
- Flash firmware(V12.5.4.0.RFBCNXM) through ADB sideload by running `adb sideload <path/to/firmware.zip>`
- Flash ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Flash Magisk (Optional)
- Go to main menu > Wipe > Format Data > Type "yes" and confirm
- Reboot and voila!

# Updating to a newer build (dirty flash):
- Flash ROM zip and magisk (optional)
- Format cache (optional, recommended)
- Reboot and voila!
