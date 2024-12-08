# Keep in mind...
- System is Read-Only (restricts making changes to overlays, system APKs, etc.)
- DO NOT USE any other recovery than PixelOS recovery which is included.
- You MUST format data with given PixelOS recovery.
- YOU MUST CLEAN FLASH if you are coming from any other ROM or stock.
- Formatting with PixelOS Recovery (yes, I mean PixelOS Recovery ONLY) is MUST during clean flash.
- Required Firmware: Android 14 U1TD34M.94-12-7 or newer. Do not flash on Android 15 firmware.
- Any slot must not be empty, meaning if you have ever used blankflash or flashed stock ROM using RSA or got a new phone, then make sure you got any ota, otherwise don't flash!

# Clean Flash (coming from a different ROM)
- Download ROM zip and vendor_boot.img.
- Boot to bootloader.
- Run `fastboot reboot fastboot`
- Run `fastboot flash vendor_boot vendor_boot.img`
- Run `fastboot reboot bootloader`
- Run `fastboot reboot recovery`
- Format data with the recovery.
- Click apply for update.
- Run `adb sideload PixelOS*.zip`
- Reboot to system.

# Dirty Flash / Update
There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.
- Download ROM zip.
- Boot to recovery.
- Click apply for update.
- Run `adb sideload PixelOS*.zip`
- Reboot to system.
