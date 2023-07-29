# Clean flash:
- Reboot to bootloader
- Flash boot, vendor_boot and dtbo images
- Reboot to recovery
- Sideload ROM zip
- Format data
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
