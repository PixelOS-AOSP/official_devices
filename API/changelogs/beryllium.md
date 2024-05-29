# 29-May-2024
- Switch to lineage libperfmgr

# 12-May-2024
- Fixed Issues with VP9 decoder
- Update XiaomiParts to QPR2
- Switch to usb 1.3 service
- Update Media codecs
- Misc Improvements

# 25-Jan-2024
- Fixed youtube autoplay issue
- Fixed google recorder mic detection issue

# 31-Dec-2023
- Switched To Retrofit Dynamic Partitions 
- Fixed Youtube & Chrome Video Lags 
- Implemented Lineage Charge Control 
- Moved Overlays to Product Partition 
- IR Face Unlock is back

# 28-Nov-2023
- Initial build based on Android 14

# 14-Oct-2023
- Dropped Kprofiles
- Added Charge Control
- Enabled to set multiple vibration intensity levels

# 20-Aug-2023
- Included miuicamera
- Removed devicesettings dependency

# 06-Jul-2023
- Tweaked statusbar padding a bit
- Relaxed charging mitigation
- Remove FM tuner from input devices
- Fixed adaptive LDAC
- Removed redundant color modes

# 11-May-2023
- Fixed adaptive LDAC
- Remove FM tuner from audio input devices to fix google recorder
- Tweaked status bar padding
- Set USB product string to Xiaomi Pocophone F1
- Set hotspot default ssid to Xiaomi Pocophone F1
- Added overlay for available color modes

# 17-Apr-2023
- Fixed a few banking apps detecting root

# 14-Apr-2023
- Enable ro.hwui.render_ahead and set it to 20 frames
- Fix fingerprint wakeup animation
- Fix a rare crash of dirac
- Disabled UI touch by default
- Disabled status bar burn in protection
- Tweaked padding a bit

# 16-Feb-2023
- Statusbar padding tweaked
- Unnecessary thermal profiles dropped
- Compiled with Playground Clang 17
- Removed Moto Dolby
- Unlocked Aperture cam additional framerates
- Disabled banking apps detecting root in init
- Mlipay support has been dropped
- Fixed hyper orange nightlight
- Switch back to prebuilt USB configurations
- Kcal support added via kernel
- Brought back stock beryllium fingeprint

# 23-Jan-2023
- Removed GcamGO and added Aperture
- Updated Dolby
- Moved to Proton Clang
- Changed kernel to perf
- Fixed issue with offline charging indicator

# 18-Nov-2022
- Updated kernel to latest linux tag
- Switched to legacy sepolicy_vndr
- Fixed rounded corners in hide notch
- Some under the hood changes

# 21-Oct-2022
- Updated SilverCore Kernel to 4.9.325 linux tag

# 12-Aug-2022
- Updated kernel to latest linux tag
- Removed top app boost
- Dropped VulkanUI renderer support
- Silenced FC spam on google TTS service

# 08-July-2022
- Updated SilverCore Kernel to latest version
- Added Clear Speaker support
- Fixed screen record stutter sometimes

# 18-June-2022
- Synced with latest PixelOS source
- Added Hide Notch
- Switch to skiaglthreaded renderthread backend
- Move renderengine to threaded skia

# 14-June-2022
- Synced with latest PixelOS source
- Updated SilverCore Kernel to latest version
- Added system_ext support
- Dropped support for Snapdragon Camera
- Shipped with Graphene Camera
- Tweaked powerhint
- Disabled Vsync for CPU rendered apps

# 10-May-2022
- Synced with latest PixelOS source
- Updated SilverCore Kernel to latest version
- Switched to AOSP Clang

# 1-May-2022
- Synced with latest PixelOS source
- Updated SilverCore Kernel to latest version
- Added separate tile for Dirac

# 10-April-2022
- Initial stable build based on Android 12.1
- Updated SilverCore Kernel to latest version
- Added some new audio equalizer presets and new earphone types
