# 24-Jul-2024
- Source upstream

# 30-May-2024
- Source upstream

# 11-May-2024
- Fixed an issue where realme link app would crash

# 21-Apr-2024
- Improved battery life and performance
- Finetuned statusbar padding
- Updated blobs, firmware and OplusCamera to MT2111_14.0.0.600(EX01)
- Updated Carrierconfig from MT2111_14.0.0.500(EX01)
- Migrate to AIDL Sensor HAL
- Improve Dolby Atmos

# 29-Feb-2024
- Updated blobs from OxygenOS 14 MT2111_14.0.0.212(EX01)

# 29-Jan-2024
- Updated blobs from OxygenOS 14.0.0.211(EX01)
- Bring back support for 32bit apps
- Fixed issues with DRM apps such as netflix
- Set default hotspot name
- Fixed WIfi Display
- Fixed an issue where some apps won't install on manual installation

# 22-Dec-2023
- Updated blobs from OxygenOS 14.0.0.210(EX01)
- Fixed VoWiFi
- Bring back LiveDisplay and Sunlight Mode for HBM
- Update IMS from LA.QSSI.14.0.r1-10000.01-qssi.0
- Fixed frame drops on video playback
- Define correct dimens for power button for seamless AOD transition

# 09-Dec-2023
- Updated blobs and camera from OxygenOS 14.0.0.80(EX01)
- Switched to a better Dolby Atmos implementation
- Enabled support Dolby HW decoders
- Fixed filters in oplus camera
- Improved statusbar padding
- Improved interaction boosting for better fluency
- Switched to step_wise thermal governor for better heat management

# 12-Nov-2023
- Initial Android 14 release
- Switched to 64-bit-only builds
- Disable OMX service and fully switched to QTI C2 media service

# 11-Sep-2023
- Updated device specific blobs to OxygenOS 13.1.0.591
- Fixed mic rated issues in calls and games
- Updated Adreno/Graphics blobs to LA.UM.9.14.1.r1-10300-QCM6490.QSSI13.0 (V600)
- Fixed camera viewfinder layout
- Ditched OplusGallery and patched OplusCamera to use GPhotos as default gallery
- Latest OxygenOS 13.1.0.591 firmware included
- Lots of kernel side improvements

# 29-Jul-2023
- Updated device blobs from OxygenOS 13.1.0.582
- Fixed battery drain
- Fixed heating
- Improve app launch speeds
- Improved Dolby Atmos
- Fixed issues with Airtel network
- Latest OxygenOS 13.1.0.582 firmware included

# 13-Jul-2023
- Updated blobs from OxygenOS 13.1.0.500
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

