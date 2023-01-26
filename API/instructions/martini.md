# Clean flash:
- Reboot to bootloader
- Flash boot, vendor_boot and dtbo images
- Reboot to recovery
- Sideload ROM zip
- Format data
- Reboot and voila!

# If you're coming from an aosp rom based on OOS 13:
- Reboot to bootloader
- Flash boot, dtbo and vendor_boot images
- Reboot to recovery, format data and sideload the ROM zip
- Reboot and voila!

# If you're coming from an aosp rom based on OOS 12:
- Flash OOS 13 F.13 fastboot rom and boot to it ( Get it from [__*HERE*__](https://drive.google.com/uc?id=1N-k64Es6QJqN4c-yU21dZTVyXZsn-MU1&export=download) )
- Install OOS 13 F.13 full OTA zip in system updater ( Can get from oxygen updater app by enabling [__*THEM*__](https://drive.google.com/uc?id=1N-k64Es6QJqN4c-yU21dZTVyXZsn-MU1&export=download) )
- Once done, reboot to bootloader, flash boot, dtbo and vendor_boot images
- Reboot to recovery, format data and sideload the ROM zip
- Reboot and voila!

# If you're coming from OOS 13 F.13:
- Same steps as above but skip the first step

# If you're coming from any older OOS 13/12 versions:
- Same steps as above but Install OOS 13 F.13 full OTA zip twice in system updater instead of flashing fastboot rom

# Updating to a newer build (dirty flash):
- Sideload ROM zip
- Reboot and voila!

# If sideloading rom gives error 7:
- Reboot to recovery
- Enter fastbootd
- fastboot wipe-super super_empty.img
- Enter recovery
- Sideload the rom zip
- Format data
- Reboot
