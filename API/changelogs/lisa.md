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
