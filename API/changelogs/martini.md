# 26-Jan-2023
- Switched to QTI Vibrator HAL (haptic effects are controlled in kernel now) - thanks to pjgowtham
- Enabled AOSP vibration intensity control
- Switched back to android.sensor.tilt_detector for pickup events
- Reserved space for dynamic partitions
- Allow only 5G SA for Jio carrier
- Fixed heavy active/idle drain issues for some users
- Rebased kernel on OOS 13 source - thanks to Albert Tang for his kernel source

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

