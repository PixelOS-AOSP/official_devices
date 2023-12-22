# 22-Dec-2023
- Re-adjusted status bar overlay
- Spoof Netflix to POCO F4 (Global) for HDR10
- Re-enable VoNR on Jio 5G
- Only allowed 5G SA on Jio
- Use HintManager for HWUI
- Enabled RCS
- Enabled VoNR calls support
- Enabled blur
- Bring back Bluetooth props
- Reduce refresh rate idle & touch time
- Fixed PowerOffAlarm
- [Xiaomi Parts] Added DC Dimming (Anti-flicker) & Touch controls for game
- [Xiaomi Parts] Added Per-app refresh rate
- [Xiaomi Parts] Removed Dolby

# 29-Nov-2023
- Dropped 32-bit Zygote (completely moved to 64-bit support only)
- Implemented Dolby Atmos (replacing Mi Sound/Dirac sound Enhancer)
- Re-implemented dynamic refresh rate switching
- Boosted Dex2oat (OTA update should now faster)
- Build Lineage health HAL (charging control)
- Updated Xiaomi Parts to current targeted SDK version

# 18-Nov-2023
- Initial beta fourteen build
- Shipped with LOS Aperture

# 18-Aug-2023
- Use the new auto network selection UI
- Updated MIUI Camera
- Use new Dirac logo
- Disable proximity sensor usage during doze
- Enable proximity check for touchscreen gestures

# 16-Jul-2023
- Source upstream

# 13-Jul-2023
- Updated blobs to MIUI V14.0.3.0.TLMMIXM
- Updated CarrierConfig to MIUI V14.0.3.0.TLMMIXM
- Reverted to ext4
- Kernel improvements
- Included latest global firmware
- Reported max frequency for Unity games
- Pre-enabled 5G SA & NSA
- Restored original power profiles
- Removed Tethering Offload config

# 10-May-2023
- Use IMS from renoir (Mi 11 Youth/Lite 5G)
- Switched to Hoshiyomi kernel
- Re-adjusted status bar padding
- Set screen-off schedutil ratelimits
- Set to powersave governor when device is idle (increased Deep Sleep efficiency)
- Reverted to Smooth Display toggle
- Removed Adaptive Battery CPU throttling & some other deprecated hints

# 16-Feb-2023
- Revert back to MIUI 13 blobs due to critical SMS issue

# 15-Feb-2023
- Updated blobs to MIUI V14.0.1.0.TLMMIXM
- Moved to EROFS
- Disabled AAudio MMAP (fixed audio muted or lost in some games, eg. Genshin Impact)
- Only allow 5G SA for Jio
- Built with KProfiles
- Use HintManager for HWUI
- Re-adjusted status bar padding
- Reduce the Maximum vertical offset of statusbar for burn-in protection
- Updated Nexus kernel v6 (Merged with Linux 4.19.272 tag)
- Disable SF EGL image tracking 
- Enable backpressure propagation in SF 
- Migrate power saving props to system
- Enable SSR for all subsystem types
- Adjust thread count & cpuset after setup wizard
- Fix app mode layout height for parts
- Declare power AIDL v3
- Compact & allow cached apps in the background
- Offload 24-bits playback supports mp3/aac format

# 23-Jan-2023
- Reverted back to ext4 filesystem
- Added dynamic refresh rate props
- Enabled Wide Color Gamut support
- Switched to AOSP color, HDR & WCG props
- Merged power profiles with AOSPA munch
- Switched to LineageOS Aperture with video recording frame rates unlocked
- Re-configured rounded corners & status bar overlays
- Switched to Vulkan render
- Switched to Nexus kernel (Merged with LA.UM.9.12.r1-15100-SMxx50.QSSI13.0 tag)
- Dropped SDM LiveDisplay service
- Enabled suspend to RAM
- Fixed fingerprint wake-up animation

# 17-Nov-2022
.

# 16-Nov-2022
- Initial official build


