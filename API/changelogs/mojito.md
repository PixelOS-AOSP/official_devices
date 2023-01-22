# 22-Jan-2023
- Update blobs from MIUI V13.0.11.0.SKGMIXM
- Disallow aux cam usage for Owlgram
- Switch to Aperture and configure it properly 
- Adjust statusbar padding
- Fix camera interface on ViLTE calls
- Fix mic in few 3rd party apps
- When connected to PC, it now shows "Redmi Note 10" instead of model
- Fix QTI Perf related issues (essentially fixes lags and stutters)
- More misc changes and optimizations

# 22-Nov-2022
- Fix memory related issues
 - Update Perf blobs from LA.UM.9.1.r1-11500-SMxxx0.QSSI12.0
- Update rounded corners for T
- Switched to QTI Perf
- Drop redundant props
- Other miscellaneous fixes

# 20-Oct-2022
- Switch to User builds
- Update blobs from mojito V13.0.10.0.SKGMIXM
- Sync audio props from V13.0.10.0.SKGMIXM [Fixes Mic on some apps] 
- Moved recovery to vendor_boot as per android documentations
- Bump EROFS PCluster Size
- Update to Boot Header v4
- Update to Boot Control HAL v1.2
- Improve peak brightness 
- Misc Fixes

# 13-Sep-2022
- Initial A13

# 13-Aug-2022
- Enable Project ID Quota support on userdata (Kills SDcardFS at early init!) 
- Drop ZRam support (NO custom kernel must be flashed!) 
- Configure VBSwap in DT (Kills userland worker at early init!) 
- Support F2FS compressions and garbage collector 
- Configure LZ4 as F2FS Compression algorithm
- Adjust statusbar height
- Kernel State at r16b12

# 21-Jul-2022
- fix Random Reboots due to EROFS [KERNEL]
- update vendor blobs from V13.0.9.0SKGMIXM 
- fixup Permissions of sconfig
- misc changes
- fixup kprofiles

# 27-June-2022
- Drop atrace HIDL service
- Dynamic thermal profile implementation
- Partially fix random reboot for few users
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
