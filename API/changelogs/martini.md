# 13-Jul-2023
- Updated display and bluetooth stack from LAHAINA 21000
- Switched to AIDL bluetooth audio service
- Improved aod
- Massively slowed down autobrightness ramp/decrease rates to fix occasional flickers
- Lots of kernel changes and improvements

# 14-May-2023
- Switched to user build
- Improved haptics effects
- Implemented aosp hbm replacing livedisplay sunlight mode
- Kernel upstreamed to v5.4.242
- Disabled a whole lot of debugging and logspam in kernel
- Increased touch sampling rate to the maximum of 600hz
- Switched to OSS display hal
- Updated display blobs from Sony Xperia 1 III and display postprocessing blobs from LAHAINA 20200
- Updated adreno graphics stack from LAHAINA 21000
- Update to audio HAL V7 
- Switch to aosp doze service for better lift to wake detection
- Updated thermal blobs to LAHAINA 20200
- Update IMS stack to QSSI 08600
- Enabled FUSE passthrough
- Limited AOD to 60hz
- Improved memory management

# 15-Apr-2023
- Switched to libperfmgr (Pixel Power HAL)
- Included Oplus Camera and Gallery from OnePlus 10 Pro
- Improved punch hole cutout
- Reworked display color modes

# 24-Feb-2023
- Enabled usage of blur under dev options 
- Updated carrierconfig from OOS 13
- Init script optimisations for better performance and battery life
- Enabled automatic refresh rate switching for better battery life
- Dropped a bunch of redundant services/blobs

# 26-Jan-2023
- Switched to QTI Vibrator HAL (haptic effects are controlled in kernel now) - thanks to [*pjgowtham*](https://github.com/pjgowtham)
- Enabled AOSP vibration intensity control
- Switched back to android.sensor.tilt_detector for pickup events
- Reserved space for dynamic partitions
- Allow only 5G SA for Jio carrier
- Fixed heavy active/idle drain issues for some users
- Rebased kernel on OOS 13 source - thanks to [*Albert Tang*](https://github.com/tangalbert919) for his kernel source

# 18-Dec-2022
- Updated to Android 13 blobs
- Switched to oss hwcomposer
- Fixed 4k60fps video recording
- Fixed superfast brightness ramping after proximity events, eg. while on phone call or hearing voice msg
- Increased aod brightness
- Fixed occasional flickers, eg. when toggling airplane mode qs tile

# 17-Nov-2022
- Switched to prebuilt Vibrator HAL (to replicate oos like haptics)
- Show volume panel on left side
- Relaxed dynamic refresh rate switching

# 07-Nov-2022
- Initial Android 13 Release

