# 27-June-2022
- Drop atrace HIDL service
- Dynamic thermal profile implementation
- ~~Partially fix random reboot for few users~~
- Other minor changes

# 09-June-2022
- Initial build with EROFS Formatting
- Disable rotation in 4 directions
- Configure Interaction boosts
- Update blobs from mojito V13.0.7.0.SKGMIXM
- KProfiles app to let you Configure KProfiles without root (Find it in battery settings)
- Fine-tune dimens (thanks to t.me/nayan942 )

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
- Adjusted dimens: Screenshot chip doesn't get cut off (thanks to t.me/nayan942 )

# 17-Jan-2022
- Kernel: Switch back to zsmalloc as default zpool storage compressor, Fixes apps force closing due to RAM issues. (thanks to t.me/NTJSM44)  for pointing it out 
- [Source] Gestures: Add and enable Quick-Tap

# 15-Jan-2022
- Pulled WiFi Configs from stock
- Fixed an issue where it's laggy due to RAM Issues
- Removed zram and fully replaced with vbswap
- Kernel: Stop spoofing vbswap as zram (thanks to t.me/cyberknight777)
- Kernel: linked with lld 13.0.0
- Vibrator: Reverted changes
- Partition: Reverted back to proper GApps partition sizes

# 01-Jan-2022
- Initial Stable Android 12
