# 26-Jan-2024
- Fixed screen recording

# 17-Jan-2024
- Source upstream

# 25-Dec-2023
- Initial Android 14 beta release
- Retrofitted dynamic partitions
- Enabled new file encryption FBE V2
- Enabled casefolding and FUSE passthrough
- Merged 'LA.UM.9.1.r1-14900-SMxxx0.QSSI14.0' in kernel
- A lot of other improvements and fixes

# 18-Aug-2023
- Fixed back tap causing SystemUI restart
- Disable proximity sensor usage during doze
- Enable proximity check for touchscreen gestures
- Fixed Facebook Marketplace's font not visible
- Refined CPU input boost parameters
- Remove CPUFreq times driver
- Set GPU idle  timeout to 64ms

# 09-Jul-2023
- Fixed offline charging animation
- Configure and enable CPU input boost
- Enabled force fast charge

# 07-Jul-2023
- Source upstream

# 05-Jul-2023
- Tune and enabled SLMK
- Misc changes in kernel

# 09-May-2023
- Disabled combined QS header
- Use pie chromatix libs for better camera quality
- Improved cpusets and cpufreq governor ratelimits
- Fixed portrait mode crash in MIUICamera
- Updated kernel to latest CLO revision (13400-SMxxx0)

# 14-Apr-2023
- Dropped Livedisplay (we've kcal and HBM in parts)

# 15-Feb-2023
- Switched back to stock adreno stack

# 22-Jan-2023
- Kernel updated to latest CLO revision
- Fixed fast charging on Chinese variants
- Fixed 48MP mode in miui camera
- Updated GPU drivers from latest sm8450 release
- Updated telephony stack to android 13
- Updated qcom media/display stack to latest CLO revision
- Switched HWUI renderer back to default (skiagl) to fix green artifacts in videos
- Misc optimizations and fixes.

# 24-Oct-2022
- Upstreamed kernel to v4.14.295
- Added missing AIDL QTI thermal HAL
- Addressed a few denials
- Extended buffer size to 256kb for offload playback
- Increased In-call earpiece volume
- Added blkio tuning from sunfish
- Switched back to stock adreno stack
- Fixed NFC (for willow users)

# 11-Sep-2022
- Initial Android 13 release

# 12-Aug-2022
- Switched back to skiagl renderer (fixed artifacts in Instagram etc.)
- Fixed expanded QS padding

# 8-Jul-2022
- Switched to vulkan UI renderer
- Switch back to stock adreno stack (WAIPIO adreno stack caused some games to crash)

# 19-Jun-2022
- Finetuned statusbar padding

# 11-Jun-2022
- Fixed some issues with biometrics
- Dropped spoof for Recorder App

# 9-Jun-2022
- Upstreamed kernel to 4.14.282 ALS
- Merged tag LA.UM.9.1.r1-11900-SMxxx0.0 in kernel
- Dropped redundant RenderScript implementation
- Updated deprecated screen power items

# 6-May-2022
- Introduced MGLRU (better memory management)
- Update telephony from LA.QSSI.12.0.r1-06500 
- Upgrade adreno stack to WAIPIO 12200
- Enabled unspecialized app process pool
- Disabled 48MP mode in MIUI Camera
- Merged android-4.14-stable (4.14.277) in kernel
- Merged tag LA.UM.9.1.r1-11800.05-SMxxx0.QSSI12.0 in kernel
- Misc optimizations in kernel 

# 26-Apr-2022
- Added fingerprint shutter for MIUI Camera
- Merged android-4.14-stable (4.14.276) in kernel
- Introduced live display

# 9-Apr-2022
- Merged April Security Patch

# 3-Apr-2022
- Fixed android Ester egg

# 1-Apr-2022
- Initial build based on Android 12.1
- Finetuned status bar padding
- Merged android-4.14-stable (4.14.272)

# 12-Mar-2022
- Updated MIUI stock blobs from V12.5.2.0.RCOMIXM
- Updated indo translation for XiaomiParts
- Upstreamed kernel to 4.14.271

# 12-Feb-2022
- Enabled quicktap
- Fixed status bar padding on lockscreen 
- Enabled USB fastcharging by default
- Merged tag 'LA.UM.9.1.r1-11600-SMxxx0.0' in kernel
- Upstreamed kernel to 4.14.265

# 15-Jan-2022
- Upstreamed kernel to v4.14.262

# 01-Jan-2022
- Switched to pixel libperfmgr for boosting
- Fixed UI glitches completely 
- Switched XiaomiParts from ArrowOS
- Switch back to Skia UI renderer
- Finetuned statusbar side padding
- Update stock blobs from V12.5.1.0.RCOMIXM 
- Added MIUI Camera (with working portrait mode)
- Upstreamed kernel to v4.14.256
- Merged latest CAF tag in kernel
- Fixed wifi and bluetooth mac address
- Removed useless QTI PASR feature
- Enabled FUSE passthrough mode
- Disabled broken zygote USAP pool
- Misc optimizations and fixes

# 27-Nov-2021
- Initial Stable build based on Android 12
