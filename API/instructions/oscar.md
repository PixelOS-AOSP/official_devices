1. Reboot to bootloader.
2. Connect your phone to the PC.
3. Download the modem.img for your device (you can find them under the 'Archive' in website):
   - OnePlus Nord CE 2 Lite:- modem_C.29_nordce2lite.img
   - Realme 9 Pro:- modem_C.10_realme9pro.img
5. Run the following fastboot commands:
   -  `fastboot flash boot boot.img`
   -  `fastboot flash vendor_boot vendor_boot.img`
   -  `fastboot flash dtbo dtbo.img`
   -  `fastboot flash --slot=all modem modem.img`
   -  `fastboot reboot recovery`
6. Select "Factory reset" and confirm.
7. Click "Advanced options" and Reboot to Recovery.
8. Select "Apply update and Apply from ADB".
9. Sideload the PixelOS*.zip using ADB: `adb sideload PixelOS*.zip`
10. Click "No" after completion and Reboot to system.
