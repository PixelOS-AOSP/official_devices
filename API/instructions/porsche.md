# Clean flash:
- I recommend being on RealmeUI 4.0 firmware version C.14 or newer before flashing
  to avoid any possible issues.
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
