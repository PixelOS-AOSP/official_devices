# 08-May-2022
- Initial Stable Android 12.1

# 14-Feb-2022
- Fix Themed boot-animation 
- Fix Always On Display flickers

# 11-Feb-2022
- Nuke Xiaomi Parts
- Neternels Bleeding Edge 
- Prebuilt lib64/libcameraservice
- Switch to GCamGOV2  
- Kernel side fixes for delayed fingerprint unlock
- Adjusted dimens: Screenshot chip doesn't get cut off thanks to @nayan942

# 17-Jan-2022
- Kernel: Switch back to zsmalloc as default zpool storage compressor, Fixes apps force closing due to RAM issues. Thanks to @NextZen86 for pointing it out 
- [Source] Gestures: Add and enable Quick-Tap

# 15-Jan-2022
- Pulled WiFi Configs from stock
- Fixed an issue where it's laggy due to RAM Issues
- Removed zram and fully replaced with vbswap
- Kernel: Stop spoofing vbswap as zram (thanks to @cyberknight777)
- Kernel: linked with lld 13.0.0
- Vibrator: Reverted changes
- Partition: Reverted back to proper GApps partition sizes

# 01-Jan-2022
- Initial Stable Android 12
