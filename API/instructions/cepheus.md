# Keep in mind: 
- Xiaomi Mi 9 (Cepheus) PixelOS builds are using Retrofit Dynamic Partitions, so, do NOT use TWRP or OrangeFOX, those recoveries on Cepheus doesn't supports these builds.
- Use PixelOS Recovery only.
- Do NOT flash custom kernels, they won't boot.
- YOU MUST CLEAN FLASH if you are coming from any other ROM or MIUI.

# Clean Flash
- Make sure your platform-tools (adb and fastboot) are up to date
- Download PixelOS Rom zip
- Download PixelOS Recovery
- Download super_empty.img (look at SourceForge or XDA for this img)
- Flash recovery using: fastboot flash recovery <recoveryname.img>
- Reboot to recovery
- Go to Advanced > Enter fastboot 
- Connect your phone to your PC and enter the following command: fastboot wipe-super super_empty.img
- If you get Unknown Command error, use: ./fastboot wipe-super super_empty.img 
- (if the above issue persists, make sure that your platform tools and drivers are up to date). 
- Press "Enter Recovery" on your phone
- Format data with Factory Reset > Format data/factory reset
- Sideload the zip with Apply Update > Apply from ADB, and do: adb sideload <ROM zip file>
- Reboot and voila!
 
# Dirty Flash
- Update via OTA updater and done or...
- Download ROM.zip from website
- Enter PixelOS Recovery > Apply Update > Apply from ADB 
- Sideload the ROM using: adb sideload <ROM zip file>
- Reboot
