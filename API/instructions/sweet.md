# Keep in mind...
This ROM comes with EROFS formatting, due to which:
- Do NOT change the kernel 
- System is Read-Only (restricts making changes to overlays, system APKs, etc. directly, however you can replace stuff with Magisk)

- Avoid using any other recovery than PixelOS recovery or the OrangeFox build (by me only!) for clean flashing so F2FS compression works
- YOU MUST CLEAN FLASH if you are coming from any other ROM or MIUI

# Clean flash:
- Flash the recovery
- Download the ROM
- Reboot to recovery
- Flash the latest MIUI 14 firmware for your region
- Flash ROM zip
- Format data
- Reboot and voila!

# Updating to a newer build (dirty flash):
- Update via OTA Updater, or
- Flash ROM zip (sideload)
- Reboot and voila!
