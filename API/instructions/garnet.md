# Prerequisites:
- Ensure you are on Latest A16/HyperOS 3.0 FW.

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
