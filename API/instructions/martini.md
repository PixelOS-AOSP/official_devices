# Clean flash:
- I recommend being on OxygenOS firmware version 13.1.0.500 or newer before flashing
  to avoid any possible issues.
- Reboot to bootloader
- Flash boot, vendor_boot and dtbo images
- Reboot to recovery
- Sideload ROM zip
- Format data
- Reboot and voila!

# Updating to OOS 13.1 firmware:
- Flash OOS 13.1.0.500 fastboot rom and boot to it ( Get it from [__*HERE*__](https://www.androidfilehost.com/?fid=10620683726822055714) )
- Install OOS 13.1 full OTA zip in system updater (Get it from "Oxygen Updater" app form playstore)
- Once done, reboot to bootloader, flash boot, dtbo and vendor_boot images
- Reboot to recovery, format data and sideload the ROM zip
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
