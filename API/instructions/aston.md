# Prerequisites:
- Must be on OxygenOS(12R) 14.0.0.810 or above
- If you are already on V14.0.0.810 or above, flash the same update again so that both slots have same firmware in them

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
