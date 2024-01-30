# 30-Jan-2024
- Source upstream

# 31-Dec-2023
- Updated device blobs from MIUI V14.0.4.0.TKQMIXM
- Updated common blobs from sweet V14.0.9.0.TKFMIXM
- Introduced Dolby Atmos (A XiaomiParts implementation)
- Update and label public libraries from sweet V14.0.7.0.TKFMIXM
- Fixed an issue where the autobrightness transition was not smooth after using MiuiCamera
- Set debug.sf.auto_latch_unsignaled to 0
- Disabled frame rate override feature
- Added missing ADSP modules
- Fix PowerOffAlarm (where the phone used to reboot before the alarm even when the phone was on)
- Move to QTI health AIDL service
- Enable usage of dex2oat64
- Import missing qcrild dependency
- Target current sdk for XiaomiParts
- Refactor ClearSpeakerFragment code
- Add {navigation,video} thermal profiles
- Updated VantomKernel
- Other misc. changes

# 31-Aug-2023
- As mentioned in the instructions, a clean flash is mandatory from the May 2023 build
- Update blobs from MIUI V14.0.3.0.TKQMIXM
- Update audio configs from MIUI V14.0.3.0.TKQMIXM
- Added MiuiCamera from MIUI V14.0.3.0.TKQMIXM
- Adjusted status bar and rounded corner padding
- SDCardFS Deprecation
- Enabled case folding support on userdata
- Use FUSE passthrough by default
- Updated Adreno to Moto G84 (bangkk)
- Enabled full LTO
- Switched to adrian-clang
- Various other device tree and kernel changes

# 11-May-2023
- Updated common blobs from sweet V14.0.2.0.TKFMIXM
- Disabled combined QS header
- Ignore CNE in location indicator
- Properly labelled fpc wakeup node 
- Disabled SF client composition cache
- Switched to unsignaled buffer latching with AutoSingleLayer
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

# 18-Apr-2023
- Updated device blobs from MIUI V14.0.2.0.TKQMIXM
- Updated common blobs from sweet V14.0.1.0.TKFMIXM
- Repatched IMS from sweet V14.0.1.0.TKFMIXM
- Updated Adreno to LA.UM.9.14.r1-21000-LAHAINA.QSSI13.0
- Fixed EGL symlink
- Updated XiaomiParts translations
- Updated VantomKernel

# 15-Feb-2023
- Updated common blobs from sweet V14.0.1.0.TKFEUXM
- Added translations for XiaomiParts
- Kernel upstream, compiled with clang 17

# 31-Jan-2023
- Updated stock blobs from MIUI V13.0.11.0.SKQMIXM
- Update common blobs from sweet V13.0.15.0.SKFMIXM
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
- Updated common blobs from sweet V13.0.16.0.SKFEUXM
- Updated XiaomiParts from lisa
- Updated power-libperfmgr
- Updated VantomKernel
- Various other misc. changes

# 29-Oct-2022
- Initial Android 13 release

# 12-Aug-2022
- Update blobs from sweet V13.0.12.0.SKFMIXM
- Fixed some RAM-related issues
- Fixed Fingerprint Wake-up Animation
- Few changes regarding vibration
- Upstreamed kernel to 4.14.290
- Fixed some freezes
- Merged CLO tag LA.UM.9.1.r1-12100.01-SMxxx0.QSSI13.0
- Various other misc. changes

# 18-July-2022
- Always on Display and Ambient Display will now run at 60hz
- Fixed an issue with the microphone being too quiet in some apps
- Fixed an issue where the google recorder didn't want to work for some users
- Enable 24-bit audio for primary output and deep buffer
- Disabled IORAP
- Possibly fixed some issues with smp2p-sleepstate
- Disabled CFI due to causing issues regarding performance 
- Upstreamed kernel to 4.14.288
- Other improvements and changes

# 12-July-2022
- Rebased on the latest xiaomi-sm6150 sources
- Switched to QTI bluetooth
- Added ANXCamera and fixed an issue where AI mode caused CPU to be stuck on maximum frequency
- Fixed PixelOS recovery not being able to flash stuff like Magisk
- Fixed a few issues with the microphone (R.I.P. Dolby)
- Labeled new wake-up nodes
- Fix-up more sepolicy
- Upstreamed kernel to 4.14.287
- Enabled Ultra Low Power State Mode on suspend
- Other misc. changes and fixes

# 26-June-2022
- Switched to user builds
- Updated courbet blobs from miui_COURBETGlobal_V13.0.8.0.SKQMIXM
- Updated common blobs from miui_SWEETEEAGlobal_V13.0.10.0.SKFEUXM
- Added thermal profiles
- Added Neural Networks and Snapdragon Computer Vision Engine stack
- Updated media configs
- Change cache partition to f2fs
- Labeled more wakeup nodes
- Switch SchedTune to UClamp
- Updated VantomKernel
- Other misc. changes and fixes

# 09-June-2022
- Updated blobs from MIUI V13.0.8.0.SKFMIXM
- Switched to EROFS (Enhanced read only file system)
- Enabled F2FS compression (Needs a clean flash to work)
- Added Moto Dolby with a tuned configuration from MIUI on the Redmi Note 10 Pro (Thanks helenius147)
- Optimize native executables for Cortex-A76 CPU
- Switch to dot product CPU variant
- Improved vibrations
- Nuked Vulkan (due to some heating/drain)
- Fixed picture adjustment in LiveDisplay (Do NOT change kernel if you want LiveDisplay to function properly)
- Fixed the remaining stuff in miuicamera like clone mode (thanks to Adarsh) P.S. slow-mo is still dead
- Updated VantomKernel and PlayGround clang
- Other misc. changes

# 15-May-2022
- Initial official and stable build based on Android 12L
