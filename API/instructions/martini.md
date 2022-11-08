# Clean flash:
- Reboot to bootloader
- Flash boot, vendor_boot and dtbo images
- Reboot to recovery
- Sideload ROM zip
- Format data
- Reboot and voila!

# If sideloading rom gives error 7:
- Reboot to recovery
- Enter fastbootd
- fastboot wipe-super super_empty.img
- Enter recovery
- Sideload the rom zip
- Format data
- Reboot

# For those who are coming from OOS13 open beta or those who downgraded from OOS13 to OOS12:
- Please follow the instructions [_`HERE`_](https://telegra.ph/Rollback-from-oos13-11-05)
- If you don't understand please come to the device group and ask for help
- I'm not responsible for any bricked devices if you fail to follow it properly

# Updating to a newer build (dirty flash):
- Sideload ROM zip
- Reboot and voila!
