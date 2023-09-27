# First Time Install / Clean Flash from Another ROM

- Reboot to Fastboot
- Flash the following imgs:
  - fastboot flash boot boot.img
  - fastboot flash dtbo dtbo.img
  - fastboot flash init_boot init_boot.img
  - fastboot flash vendor_boot vendor_boot.img
  - fastboot flash vendor_kernel_boot vendor_kernel_boot.img
- Go to Recovery Mode
- FORMAT DATA . (Requires full backup of internal storage)
- Go to "Apply Update - Adb Sideload"
- Flash the ROM
- Reboot to System and #PixelOS

# Update / Dirty Flash

- Reboot to Recovery
- Go to "Apply Update - Adb Sideload"
- Flash the ROM
- Reboot to System and #PIxelOS
