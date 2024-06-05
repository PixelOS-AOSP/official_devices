# 05-Jun-2024
- Switch to lineage libperfmgr

# 15-May-2024
- Removed Spatial Audio
- Removed Soundtrigger related stuff
- Switched to OSS audio
- Adjusted statusbar padding

# 30-Apr-2024
- Moved to OSS audio
- Added back dolby

# 16-Feb-2024
- Source upstream

# 23-Jan-2024
- Fixed high vibration intensity  
- Adjusted status bar padding  
- Removed miui camera

# 23-Dec-2023
- Initial build

# 02-Oct-2023
- Switched to power-libperfmgr
- Reduced device boot time
- Switched to Pixel Thermal
- Removed Kcal in favor of LiveDisplay

# 18-Aug-2023
- Switch to DFC kernel
- Bring in XiaomiParts
- Drop legacy DRM hal
- Move dolby to XiaomiParts
- Double tap sensor now needs a proximity check
- Disabled statusbar burn-in protection
- Move to Xiaomi sensors Multi-HAL
- Disabled livedisplay
- Dropped Mlipay support

# 06-Jul-2023
- Cleaned up sepolicy and removed duplicate labels
- Fixed wakeup labels
- Fully switched to jemalloc 
- Set powersave governor when the device is idle for better deep sleep
- Added Oneplus dolby
- Removed Dirac
- Enabled config_avoidGfxAccel

# 11-May-2023
- Removed prebuilt Firmware
- Switched to Prebuilt audio HAL- Remove FM tuner from input devices
- Added missing ACDB IDs
- Switch to DEFAULT_MEDIA_VOLUME_CURVE for music and ring
- Unlocked Aperture video additional framerates
- Improved status bar padding
- Renamed hotspot SSID to Miatoll
- Configure default light sensor type 
- Cleanup Dirac headphone types
- Removed Clear Speaker
- Removed Doze service
- Enable ro.hwui.render_ahead and set it to  3 frames
- Use HintManager for HWUI
- Set to powersave governor when device is idle 
- Fix missing frequency in power_profile
- Update GPU idle timeout to 64ms

# 19-Apr-2023
- Fix low mic volume on reception end in loudspeaker and wired earphones
- Fix some banking apps detecting root

# 15-Apr-2023
- Add Dirac sound enhancer
- Fixed carrier aggregation
- Enable ro.hwui.render_ahead and set it to 20 frames
- Remove no longer needed aptX blobs
- Removed prebuilt gcam and brought back Aperture

# 27-Jan-2023
- Switched to Alex tree

# 06-Nov-2022
- Initial Android 13 build

# 18-Aug-2022
- Fixed black screen flicker (SOD)
- Enabled FUSE Passthrough
- Hid Magisk Better

# 14-July-2022
- Fixed DT2W
- Adjusted statusbar padding
- Tons of under the hood misc changes

# 19-June-2022
- Initial Build Release
