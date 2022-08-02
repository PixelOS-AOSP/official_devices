# Clean Flash
- Make sure your platform-tools (adb and fastboot) are up to date
- Download PixelOS Rom zip
- Download PixelOS Recovery
- Download super_empty.img (look at XDA for this img)
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
- Update via ota updater and done.or,
- Download ROM.zip from website
- Enter PixelOS Recovery > Apply Update > Apply from ADB 
- Sideload the ROM using: adb sideload <ROM zip file>
- Reboot

# Do not use TWRP or OrangeFOX, those recoveries on Cepheus doesn't support FBEV2 encryption.
