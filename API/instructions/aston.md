# Prerequisites:
- Device must be running OxygenOS(12R)/ColorOS(ACE3) version 14.0.0.810 or higher, but below OxygenOS 15.
- Flash the current build again using local install to ensure both slots have the same firmware.

# Clean flash:
- Reboot to bootloader
- Flash boot, vendor_boot, dtbo and recovery images
   -  `fastboot flash boot boot.img`
   -  `fastboot flash vendor_boot vendor_boot.img`
   -  `fastboot flash dtbo dtbo.img`
   -  `fastboot flash recovery recovery.img`
- Reboot to recovery
- Sideload ROM zip
   -  `adb sideload PixelOS*.zip`
- Format data after sideload
- Reboot and voila!

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
