**Important Warning:**
- Firmware is no longer included in the ROM zip.

- Starting with OOS 14.0.0.2900(EX01), OnePlus enabled Anti-Rollback (ARB). If you're on this firmware (or newer), flashing older stock ROMs or older PixelOS Android 16 builds can permanently brick your device because they contain older firmware.

- The Android 17 build can be flashed safely regardless of your current firmware version. If you're coming from stock ROM though, make sure both slots are on the same firmware version. The easiest way to do that is to local update your current stock ROM twice so both slots get updated.

TL;DR: Don't flash older PixelOS Android 16 builds to roll back from Android 17. Update both slots to the latest stock firmware first, then flash Android 17.
As always, you're responsible for what you flash.

**Flashing Steps:**
- Reboot to bootloader.
- Connect your phone to the PC.
- Run the following fastboot commands:
   -  `fastboot flash boot boot.img`
   -  `fastboot flash vendor_boot vendor_boot.img`
   -  `fastboot flash dtbo dtbo.img`
   -  `fastboot reboot recovery`
- Select "Factory reset" and confirm.
- Click "Advanced options" and Reboot to Recovery.
- Select "Apply update and Apply from ADB".
- Sideload the PixelOS*.zip using ADB: `adb sideload PixelOS*.zip`
- Click "No" after completion and Reboot to system.
