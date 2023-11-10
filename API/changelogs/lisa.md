# 10 November 2023
- Hotfix for Play Integrity fix

# 07-Nov-2023
- Initial beta build based on Android 14
- Fixed an issue where big and prime core would get struck on higher frequencies on idle
- Enabled MGLRU (better memory management)
- Merged tag LA.UM.9.14.r1-22400-LAHAINA.QSSI13.0 in kernel

# 30-Sep-2023
- Improved battery life and performance
- Added charging control from lineage
- Updated stock blobs from MIUI V14.0.6.0.TKOMIXM
- OTA Updater is now faster

# 29-Aug-2023
- Enable secure NFC
- Fixed auto brightness behavior  
- Fixed weird glitches on apps like YouTube
- Merged tag LA.UM.9.14.r1-22200-LAHAINA.QSSI14.0 in kernel
- Minor improvements and fixes

# 17-Aug-2023
- Improved speed of biometric authentication methods (face unlock, fingerprint)
- Set default model name for USB device
- Resolved issue with rapid decrease in brightness under adaptive brightness
- Miscellaneous improvements and fixes.

# 19-Jul-2023
- Fixed CTS profile match not passing (Safetynet)

# 18-Jul-2023
- Updated IMS stack to LA.QSSI.13.0.r1-10000.02-qssi.0 
- Updated blobs and MIUiCamera to miui_LISAGlobal_V14.0.4.0.TKOMIXM
- Fixed an issue where hotspot would take several attempts to turn on
- Set correct device name and hotspot SSID 
- Fixed MIUICamera crash on CN models

# 05-Jul-2023
- Switched to QTI WiFi Display
- Included latest global stable firmware
- Update IMS blobs from LA.QSSI.13.0.r1-10000.02-qssi.0
- Added MGLRU for better memory management
- Fixed an issue where auto brightness ramps up randomly after the last update
- Performance improvements
- Misc improvements and fixes.

# 10-May-2023
- Switched to pixel libperfmgr for boosting
- Fixed ViLTE (carrier video calling)
- Updated MIUICamera from MIUI V14.0.3.0.TKOINXM
- Fixed clone mode in MIUICamera
- Updated CarrierConfig from MIUI 14
- Reverted back to stock GPU peak frequency
- Switched back to HWC for brightness control
- Fixed issues with Google recorder
- Merged 'LA.UM.9.16.r1-13000-MANNAR.QSSI12.0' tag in kernel
- Misc improvements and fixes.

# 19-Apr-2023
- Fixed safetynet issues for non root users
- Updated stock blobs MIUI V14.0.3.0.TKOMIXM

# 13-Apr-2023
- Fixed an issue where blacks were displayed as grey in apps like Netflix
- Fixed an issue where stock camera app would force close randomly
- Fixed media playback in browsers and a few more apps like Twitter
- Updated kernel to latest CLO tag
- Misc. fixes and improvements

# 16-Feb-2023
- Updated fingerprint and desc. from MIUI 14

# 15-Feb-2023
- Updated stock blobs and configs from MIUI V14.0.2.0.TKOMIXM
- Updated MIUI Camera from MIUI V14.0.2.0.TKOMIXM
- Switched back to stock adreno stack
- Enabled anti-aliasing for notch cutout and corners
- Added support for aux on Aperture camera
- Misc. improvements and fixes

# 29-Jan-2023
- Fixed random reboots
- Dropped Livedisplay (doesn't work properly on sm8350 devices)
- Added back boosted color profile (dropped sRGB and P3)
- Updated kernel to CLO tag 'LA.UM.9.14.r1-21000-LAHAINA.QSSI13.0'
- Updated wireguard to v1.0.20220627

# 23-Jan-2023
- Fixed bluetooth LE (low energy) audio
- Fixed HDR video playback on Netflix
- Added P3 and sRBG color profiles
- Improved battery backup ;)
- Updated stock blobs from MIUI13 SKOMIXM.13.0.8.0
- Improved refresh rate switching
- Locked refresh rate to 60hz on AOD
- Added picture adjustment options in livedisplay
- Enabled google dialer call recording feature
- Reworked cutout and statusbar paddings

# 27-Nov-2022
- Added support for aptX codecs
- Xiaomi Parts improvements
- Fixed an issue where some website wouldn't load
- Added support for WiFi MAC randomization

# 16-Nov-2022
- Improved battery backup
- Improved scheduler performance
- Improved brightness scaling algorithm
- Fixed low res pictures on MIUI Camera (64MP works too!)
- Fixed issues with sending compressed video files on tg
- Bumped vendor security patch level
- Added display configuration for HBM
- Drop unused 32 bit libs
- Addressed a few denials
- Misc fixes and improvements

# 23-Oct-2022
- Finetune rate limits for prime CPU
- Disable IOP properties
- Moved background cpuset to CPU 0-1
- Disabled pocket service debug
- Misc. changes and improvements

# 03-Oct-2022
- Initial Android 13 build

# 15-Aug-2022
- Reverted back to boot header v3 (try your luck with custom recoveries)
- Reverted most blobs to stock
- Reverted back to aosp color profiles as earlier 
- Nuked hi-fi as it doesn't work
- Enabled back CAF input boost
- Switched to QuickSilver Kernel

# 12-Jul-2022
- Fixed	lockscreen issues 
- Fixed random app crashes

# 11-Jul-2022
- Added OTA asserts
- Upgraded to Boot Control HAL to v1.2
- Upgraded to boot header to v4
- Fixed ViLTE calls
- Misc optimizations and fixes

# 23-Jun-2022
- Shipped MIUICamera (everything works)
- Added Hi-Fi and sound scenes to Mi sound enhancer
- Sync gps changes with LA.UM.9.14.r1-19200.02-LAHAINA.QSSI13.0
- Tonnes of misc. changes

# 18-Jun-2022
- Introduced XiaomiParts
- Fixed 5GHz hotspot
- Fixed WiFi Display
- Cleaned up audio properties
- Misc. changes

# 11-Jun-2022
- Spoofed Netflix as Pixel 6 (fixes HDR playback)
- Addressed alot of selinux denials
- Updated perf, neural networks and scve blobs from LA.UM.9.14.r1-19300.01-LAHAINA.QSSI12.0
- Optimized power consumption BT media devices
- Updated graphics blobs to WAIPIO 13100
- Updated init scripts from MIUI 13
- Switched to dot product CPU variant
- Dropped CAF boost entirely
- Optimized memory usage
- Relaxed refresh rate switching
- Used arter's vrr implementation 
- Configured audio-app cpusets
- Enabled support for 6GHz WiFi
- Added support for Network Guru
- Many more under the hood improvements and optimizations

# 13-May-2022
- Updated display stack from LA.UM.9.14.r1-19300.01-LAHAINA.QSSI12.0
- Added support for Dolby Vision
- Updated adreno drivers to V615
- Switched back to QTI Perf from libperfmgr
- Updated media configs from MIUI 13.0.4 Global
- Addressed a bunch of denials
- Charging speed and temp management should be better now
- Fixed fingerprint location indicator
- Fine tuned autobrightness ramp rates
- Imported few missing blobs 
- Enabled QCRIL radio power saving
- More misc improvements
- tl;dr better battery, performance and less heat 

# 1-May-2022
- Updated blobs from MIUI 13.0.4 Global Release
- Switched to Pixel Power HAL (libperfmgr)
- Fixed all camera and video recording related issues
- QR code scanner and gpay should be fine too now
- Fixed ANXCamera crash
- Updated deprecated screen power items 
- Fixed slow boot time
- Fixed secure_element logspam
- Fixed deep sleep issues with aod, device now enters deep sleep with aod turned on
- Addressed a few more denials
- Updated WiFi overlay and configs from MIUI 13 (hopefully WiFi connectivity issues are resolved)
- Enabled the usage of Vulkan 
- Many more misc improvements

# 11-Apr-2022
- Merged April Security Patch (android-12.1.0_r4)
- Update most stock blobs from MIUI 13 Lisa
- Updated audio and media configs from MIUI 13
- Shipped MIUI Global Stable firmware with the ROM
- Switched to Atom X kernel
- Get rid of HD capable SIM notification
- Minor fixes and improvements

# 13-Mar-2022
- Initial OSS build
- Enforcing SELinux

# 22-Jan-2022
- Initial build based on Android 12
- Permissive SELinux
