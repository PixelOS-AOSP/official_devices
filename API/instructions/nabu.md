# Keep in mind...
- DO NOT USE any other recovery than TWRP recovery which is linked in the XDA thread.
- YOU MUST CLEAN FLASH IF:
    - You are coming from any other ROM or MIUI
    - You are coming from previous Android Version
- Magisk should only be flashed after booting once into the ROM. Do not flash Magisk along with the ROM package
- Do not flash Hyper OS firmware. Use the latest available MIUI firmware.

- If you face issues like poor RAM management or storage issues, you have not followed the instructions and/or have changed kernel/recovery. STRICTLY follow the instructions provided again before reporting any issues.

# Clean Flash (coming from a different ROM) (Using TWRP)
Clean flash involves formatting data which means you will be loosing data stored in the internal storage of your device, data in SD Card should not be affected. I will not be responsible for any loss of data.
- Download ROM
- Reboot the device to Recovery mode by powering off the device and then by holding Power button and Volume UP key together
- Go to Wipe > Advanced Wipe > Wipe dalvik cache, Data, Metadata
- Press home button in TWRP > Tap on Install > Navigate to path where you have downloaded the ROM > Flash the ROM
- Make sure to enable the checkbox "Automatically Reflash TWRP after flashing a Rom"
- Press back button in TWRP > Navigate to path where you had stored Firmware file > Flash Firmware
- Go to Wipe > Format Data > type "yes" > Press Enter (tick mark)
- Reboot and voila!

# Dirty Flash / Update (Using TWRP)
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM file to your computer
- Reboot the device to recovery
- Tap on Install > Navigate to path where you have downloaded the ROM > Flash the ROM
- Press back button in TWRP > Navigate to path where you had stored Firmware file > Flash Firmware
- Reboot and voila!

# Clean Flash (coming from a different ROM) (Using PixelOS/AOSP recovery)
Clean flash involves formatting data which means you will be loosing data stored in the internal storage of your device, data in SD Card should not be affected. I will not be responsible for any loss of data.
- Download ROM, vendor_boot and boot files to your computer (click on recovery button for vendor_boot and boot)
- Reboot the device to bootloader (Fastboot Mode)
- Flash the vendor_boot by running `fastboot flash vendor_boot <path/to/vendor_boot.img>` in terminal
- Flash the boot by running `fastboot flash boot <path/to/boot.img>` in terminal
- Reboot to recovery by running `fastboot reboot recovery` in terminal
- Go to main menu > Factory reset > Format data/factory reset >  Format data >  Back to Main menu > Reboot to Recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Flash firmware through ADB sideload by running `adb sideload <path/to/firmware.zip>` in terminal
- Reboot and voila!

# Dirty Flash / Update (Using PixelOS/AOSP recovery)
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM file to your computer
- Reboot the device to recovery
- On your phone [which is in recovery mode], Apply update > Apply from ADB 
- Flash the ROM through ADB sideload by running `adb sideload <path/to/rom.zip>` in terminal
- Flash firmware through ADB sideload by running "adb sideload <path/to/fw.zip>" in terminal
- Reboot and voila!
