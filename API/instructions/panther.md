# First Time Install / Clean Flash from Another ROM
1. Reboot to Fastboot
2. Flash the following imgs

fastboot flash boot boot.img


fastboot flash dtbo dtbo.img


fastboot flash init_boot init_boot.img


fastboot flash vendor_boot vendor_boot.img


fastboot flash vendor_kernel_boot vendor_kernel_boot.img


4. Go to Recovery Mode
5. FORMAT DATA . (Requires full backup of internal storage)
6. Go to "Apply Update - Adb Sideload"
7. Flash the ROM
8. Reboot to System and #PixelOS

# Update / Dirty Flash
1. Reboot to Recovery
2. Go to "Apply Update - Adb Sideload"
3. Flash the ROM
4. Reboot to System and #PIxelOS