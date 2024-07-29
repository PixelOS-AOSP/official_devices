# Keep in mind:
- Use PixelOS Recovery only
- Do not use TWRP or similar (like OrangeFox and SHRP), these recoveries do not support encryption on our devices.

# Clean flash (coming from a different ROM):
- Make sure your device's bootloader is unlocked (If you are leaving stock rom)
- Power off the device and boot to download mode (Vol Down + Bixby Key + USB Cable)
- Download the recovery image for your device (present in PixelOS SourceForge)
- Rename this to recovery.img and compress it as a tar file using 7zip
- Download Samsung Odin and open it (If the device is not recognized, make sure Samsung USB Drivers are properly installed)
- Put the resultant tar file (recovery.tar) in Odin's AP slot and flash it
- At the exact moment the screen goes off, don't remove the USB Cable and boot to recovery mode (Vol Up + Bixby Key + Power)
- Download ROM from the link above
- Format data, cache and system
- Flash ROM using adb sideload or sdcard
- Flash Magisk (Optional)
- Format data, reboot and voila!

# Updating to a newer build (dirty flash):
- Flash ROM zip and magisk (optional)
- Format cache (optional, recommended)
- Reboot and voila!
