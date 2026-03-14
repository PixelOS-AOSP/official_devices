# 14-Mar-2026
- Improved memory management and performance for 4GB ram users
- Improved status bar padding
- Fixed time getting reset after reboot while not connected to internet

# 24-Feb-2026
- Shipped OnePlus Dolby
- Fixed USB tethering
- Updated Keymaster blobs from sweet_k6a
- Updated WFD system blobs from dada OS3.0.5.0.WOCMIXM
- Disabled FRP
- Patched libdpps.so to depend on libtinyxml2-v34.so
- Switched to QTI Thermal AIDL HAL
- Updated thermal configs
- Shipped Leica Camera
- Fixed touchscreen in PixelOS recovery
- Re-worked over audio configs
- Upreved audio HAL to V7
- Synced kernel with the latest LineageOS sm8150 changes.
- Fixed slow charging issue for some users

# 15-Jan-2026
- Enabled Userfaultfd (UFFD) Garbage Collection for improved memory management
- Reduced system-wide blur radius for better performance
- Moved USB MTP/PTP functionality to the USB FunctionFS (F_FS) driver
- Migrated to the QTI USB Gadget AIDL HAL
- Switched default USB tethering protocol to NCM
- Enabled support for using the device as a high-quality webcam
- Removed unnecessary virtual framebuffer to save system resources
- Removed forced DCI-P3 color gamut on adaptive color mode
- Disabled the Quick Settings media player turbulence effect by default
- Hardware revision will be shown in Settings now
- Optimized kernel and removed various debugging overheads

# 02-Jan-2026
- Addressed microphone issues that could affect call and recording quality.
- Added Bypass Charging to allow direct power delivery from the charger.
- Fixed an issue where Roboto was used instead of Google Sans.
- Synced kernel with the latest LineageOS sm8150 changes.

# 31-Dec-2025
- Initial Android 16 Build

