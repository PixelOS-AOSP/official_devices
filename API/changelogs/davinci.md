# 31-Dec-2023
- Fixed an issue where the system would have unexpected slowdowns 
- Disabled light sensor for pocket lock

# 28-Dec-2023
- Update common blobs from sweet V14.0.9.0.TKFMIXM
- Fixed offline charging animation 
- Set debug.sf.auto_latch_unsignaled to 0
- Disable frame rate override feature
- Switch BtAudio to AIDL
- Kernel upstream

# 19-Nov-2023
- Update common blobs from from sweet V14.0.8.0.TKFMIXM
- Update and label public libraries from sweet V14.0.7.0.TKFMIXM
- Fix PowerOffAlarm (where the phone used to reboot before the alarm even when the phone was on)
- Move to QTI health AIDL service
- Enable usage of dex2oat64
- Import missing qcrild dependency
- Target current sdk for XiaomiParts
- Updated VantomKernel
- Other misc. changes

# 31-Aug-2023
- Moved sku version setup to kernel
- Updated Adreno to Moto G84 (bangkk)
- Add metadata to recovery.fstab so it is formatted on factory reset
- Merged latest CLO/Linux tags in kernel
- Other misc. changes

# 09-Jul-2023
- Retrofit Dynamic partitions 
- Switched to FBEv2
- SDCardFS Deprecation
- Enabled case folding support on userdata
- Use FUSE passthrough by default
- Update CarrierConfig from  LA.QSSI.13.0.r1-10000.02-qssi.0
- Enabled full LTO
- Switched to adrian-clang
- Various other device tree and kernel changes
- A clean flash is mandatory using the PixelOS recovery

# 27-May-2023
- Updated common blobs from sweet V14.0.2.0.TKFMIXM
- Disabled combined QS header
- Ignore CNE in location indicator
- Disabled SF client composition cache
- Removed non-existent SF properties
- Do not balance msm_drm and kgsl-3d0 IRQs
- Remove max ZRAM compression streams setting 
- Drop vestigial FM board-flags
- Upgrade IImsFactory to 1.1 in manifest
- Update QTI Radio LPA HIDL to 1.1
- Uprev bluetooth audio HIDL impl to 2.1
- Remove discard command tuning
- Don't mount TraceFS twice
- Upstreamed kernel to 4.14.314
- Merge CLO tag 'LA.UM.9.1.r1-13500-SMxxx0.QSSI13.0' in kernel

# 16-Apr-2023
- Updated blobs from sweet V14.0.1.0.TKFMIXM
- Repatched IMS from sweet V14.0.1.0.TKFMIXM
- Updated Adreno to LA.UM.9.14.r1-21000-LAHAINA.QSSI13.0
- Fixed EGL symlink
- Updated VantomKernel

# 15-Feb-2023
- Updated common blobs from sweet V14.0.1.0.TKFEUXM
- Kernel upstream, compiled with clang 17

# 31-Jan-2023
- Update blobs from MIUI V13.0.15.0.SKFMIXM
- Update the Adreno stack
- Uprev IQtiRadio with v2.6
- Uprev ImsRadio version to 1.7
- Uprev Bluetooth Audio HIDL to 2.1
- Uprev IFactory version to 2.3.
- Update GPS to LA.UM.9.1.r1-13000-SMxxx0.QSSI13.0
- Revert gps PROXY_APP_PACKAGE_NAME OEM change
- Disable SF composition prediction model
- Force device to treat 170M as sRGB in SF
- Disable redir_party_num
- ViLTE should work now?
- Tons of other misc. changes

# 25-Nov-2022
- Rebased on the latest xiaomi-sm6150 sources
- Fixed screen-off UDFPS and UDFPS on AOD
- Fixed some bluetooth related issues
- Disabled light sensor for pocket lock
- Updated statusbar padding
- Updated common blobs from sweet V13.0.16.0.SKFEUXM
- Updated power-libperfmgr
- Updated VantomKernel
- Other misc. changes

# 29-Oct-2022
- Initial Android 13 release

# 12-Aug-2022
- Update blobs from sweet V13.0.12.0.SKFMIXM
- Upstreamed kernel to 4.14.290
- Merged CLO tag LA.UM.9.1.r1-12100.01-SMxxx0.QSSI13.0
- Fixed some performance related issues 
- Fixed a few freezes which occurred 
- Various other misc. changes

# 30-Jul-2022
- Update davinci blobs from MIUI V12.5.2.0.RFJCNXM
- Fixed an issue where the microphone volume was too low in a few apps such as Instagram
- Update the Adreno stack from LA.UM.9.14.r1-19300-LAHAINA.QSSI12.0
- Add Neural Networks Stack
- Updated the WiFi config
- Update a few display properties
- Fixed the Google recorder
- Updated the kernel

# 13-July-2022
- Rebased on the latest xiaomi-sm6150 sources
- Switched to QTI bluetooth
- Added Graphene Camera
- Upstreamed kernel to 4.14.287
- Enabled Ultra Low Power State Mode on suspend
- Other misc. changes and fixes

# 26-June-2022
- Switched to user builds
- Updated blobs from miui_SWEETEEAGlobal_V13.0.10.0.SKFEUXM
- Added Neural Networks and Snapdragon Computer Vision Engine stack
- Updated VantomKernel
- Other misc. changes and fixes

# 18-Jun-2022
- Fixed issues related to audio
- Updated kernel

# 09-Jun-2022
- Updated blobs from MIUI V13.0.8.0.SKFMIXM
- Update adreno from LA.UM.9.1.r1-11500.02-SMxxx0
- Switched to EROFS (Enhanced read only file system)
- Enabled F2FS compression (Needs a clean flash to work)
- Optimize native executables for Cortex-A76 CPU
- Switch to dot product CPU variant
- Nuked Vulkan (due to some heating/drain)
- Fixed picture adjustment in LiveDisplay (Do NOT change kernel if you want LiveDisplay to function properly)
- Updated VantomKernel and PlayGround clang
- Other misc. changes

# 6-May-2022
- Kernel update
- Better RAM Management

# 30-Apr-2022
- Added a few missing blobs
- Fixed anti flicker mode
- Enable zygote unspecialized app process pool
- Configure SQLite to operate in MEMORY mode
- Added MGLRU for better memory management
- Dropped SLMK in favor of LMKD
- Use LMKD from YAAP for better memory management
- Updated kernel
- Misc. changes and fixes

# 27-Apr-2022
- Changed kernel to VantomKernel compiled with PlayGround clang 15
- Updated blobs from sweet MIUI V13.0.8.0.SKFEUXM
- Introduced haptic control
- Introduced livedisplay
- Fixed WiFi Display (Miracast)
- Fixed some issues with NFC
- Increased volume steps from 15 to 25
- Misc. fixes and changes

# 10-Mar-2022
- Merged April Security Patch

# 2-Mar-2022
- Improved vibrations
- Improved UDFPS
- Configure physical power, volume and fingerprint locations
- Changed default status bar height
- HBM is now white
- Miscellaneous changes and fixes from xiaomi-sm6150

# 2-Feb-2022
- February security patch

# 16-Jan-2022
- Jan-security patch

# 02-Jan-2022
- Fixed bluetooth audio

# 01-Jan-2022
- December Security patch
- Fixed FOD on AOD
- Fixed OTA asserts
- Switched to VantomKernel
- Finetuned statusBar padding
- Fixed Hey Google voice match
- Fixed APN not getting recognized 
- Fixed camera on telegram
