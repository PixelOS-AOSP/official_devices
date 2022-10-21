# Keep in mind: 
- Since Cepheus is using Retrofit, do NOT use TWRP or OrangeFOX.
- Use PixelOS Recovery only.
- Do NOT flash custom kernels, they won't boot.
- YOU MUST CLEAN FLASH if you are coming from any other ROM or MIUI.

# Clean Flash
- Make sure your platform-tools (adb and fastboot) are up to date.
- Download PixelOS ROM zip and recovery.img.
- Reboot into Fastboot.
- Flash recovery using: fastboot flash recovery <recoveryname.img>
- Reboot to recovery.
- In recovery, format data with Factory Reset > Format data/factory reset
- Sideload the zip with Apply Update > Apply from ADB, and do: adb sideload <ROM zip file>
- Optional: Flash magisk with sideload using: adb sideload <Magisk zip> 
- ^ Magisk will show a message about "Signature verification failed, install anyways?", just click YES.
- Reboot and voila!

# Dirty Flash
- Download ROM zip
- Enter PixelOS Recovery > Apply Update > Apply from ADB 
- Sideload the ROM using: adb sideload <ROM zip file>
- Optional: sideload Magisk using: adb sideload <Magisk zip>
- Reboot and voila!
