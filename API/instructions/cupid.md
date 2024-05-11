# Keep in mind...
- DO NOT try to change the included kernel!
- Ensure you are on HyperOS firmware (V1.0.3.0.ULCEUXM+).
- Follow the appropriate section depending on which recovery you use.
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI.
    - You are coming from previous Android Version.

# Clean Flash using PixelOS Recovery (coming from a different ROM).
Clean flash involves formatting data which means you will lose your data that is stored in the internal storage of your device. I will not be responsible for any loss of data!
- Download ROM, vendor_boot, dtbo and boot files to your computer (click on recovery button for vendor_boot, dtbo and boot)
- Reboot the device to bootloader (Fastboot Mode)
- Flash the vendor_boot by running `fastboot flash vendor_boot <path/to/vendor_boot.img>` in terminal
- Flash the dtbo by running `fastboot flash dtbo <path/to/dtbo.img>` in terminal
- Flash the boot by running `fastboot flash boot <path/to/boot.img>` in terminal
- Reboot to recovery by running `fastboot reboot recovery` in terminal
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to Recovery
- Reboot and voila!

# Dirty Flash / Update using PixelOS Recovery.
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM file to your computer
- Reboot the device to recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Reboot and voila!

# Clean flash using TWRP (coming from a different ROM).
Clean flash involves formatting data which means you will lose your data that is stored in the internal storage of your device. I will not be responsible for any loss of data!
- Download ROM and SKKK's TWRP (click [here](https://sourceforge.net/projects/recovery-for-xiaomi-devices/files/cupid/twrp-3.7.1_12-v8.6_A14-cupid-skkk.img/download) to download).
- Reboot the device to bootloader (Fastboot Mode).
- Flash the TWRP image by running `fastboot flash recovery_ab <path/to/twrp.img>` in terminal.
- Reboot to TWRP by running `fastboot reboot recovery` in terminal.
- On your phone [which is now in recovery mode], select Advanced, and then ADB sideload.
- On your PC's terminal, run this command to flash the ROM: `adb sideload <path/to/zip>`.
- Navigate back to the main menu > Wipe > Format Data > Back to main menu > Reboot to system
- Voila! All done!

# Dirty flash using TWRP (coming from a different ROM).
Clean flash involves formatting data which means you will lose your data that is stored in the internal storage of your device. I will not be responsible for any loss of data!
- Download ROM and SKKK's TWRP (click [here](https://sourceforge.net/projects/recovery-for-xiaomi-devices/files/cupid/twrp-3.7.1_12-v8.6_A14-cupid-skkk.img/download) to download).
- Reboot the device to bootloader (Fastboot Mode).
- Flash the TWRP image by running `fastboot flash recovery_ab <path/to/twrp.img>` in terminal.
- Reboot to TWRP by running `fastboot reboot recovery` in terminal.
- On your phone [which is now in recovery mode], select Advanced, and then ADB sideload.
- On your PC's terminal, run this command to flash the ROM: `adb sideload <path/to/zip>`.
- Navigate back to the main menu > Reboot to system.
- Voila! All done!