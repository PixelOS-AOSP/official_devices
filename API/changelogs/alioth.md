# 13-May-2023
- Merged 4.19.282 ACK
- Update blobs to V14.0.4.0.TKHMIXM
- Rebased kernel to Immensity 
- Fixed Camera viewfinder lag
- Fixed Display goes darker when video streaming
- Increaded top-app schedtune boost
- Added dc dimming support

# 15-Apr-2023
- Switched to Smooth Display
- Dropped Qs refresh rate (We have switched to smooth display)
- Fixed Calling on some carriers
- Enhanced Audio quality
- Fixed libperfmgr spamming

# 14-Apr-2023
- Added Leica Camera
- Nuked Dolby (Just creates more issues then it improves)
- Fixed Bluetooth issues on Tik tok 
- Adjusted status bar padding
- Dropped Qualcomm WFD (Fixes wfd crashes)
- Added touch profiles
- Fixed Google Recorder
- Enabled ufs powersaving after boot
- Dropped PM QoS boosting
- Removed Audio hints
- Removed Google-specific camera hints
- Removed hints for Adaptive Battery CPU Throttling
- Enabled F2F2 background GC
- Updated pinner configuration
- Use FUSE passthrough by default
- Enabled volte on some carriers
- Stealed SurfaceFlinger offsets from taro (Decreases latency)
- Enabled use_smooth_motion

# 19-Feb-2023
- Built with Aosp Clang 17.0.0
- Built Kprofiles
- Merged 4.19.272
- Improved High Brightness Mode (HBM)
- Update CarrierConfig from LA.QSSI.13.0.r1-07400-qssi.0
- Fixed layout height on Thermal Profiles
- Updated camera cutout
- Disabled QCRIL power saving
- Fixed fingerprint wake-up animation
- Re-configured CPU variant according to GS101
- Reverted userdata tuning from oriole (Seems like decreases storage speed)
- Disabled Wallpaper Zooming
- Disabled sf EGL image tracking (To reduce overhead)
- Fixed some audio related issues
- Use AOSP default ripple animation duration

# 18-Feb-2023
- Built with Aosp Clang 17.0.0
- Built Kprofiles
- Merged 4.19.272
- Improved High Brightness Mode (HBM)
- Update CarrierConfig from LA.QSSI.13.0.r1-07400-qssi.0
- Fixed layout height on Thermal Profiles
- Updated camera cutout
- Disabled QCRIL power saving
- Fixed fingerprint wake-up animation
- Re-configured CPU variant according to GS101
- Reverted userdata tuning from oriole (Seems like decreases storage speed)
- Disabled Wallpaper Zooming
- Disabled sf EGL image tracking (To reduce overhead)
- Fixed some audio related issues
- Use AOSP default ripple animation duration

# 22-Jan-2023
- Merged 4.19.269
- Fixed rounded corners
- Added aperture lens and aditional videos framerates
- Switch to Vulkan render
- Added high touch polling rate
- Fixed AOD flicking
- Disabled kpti
- Enabled zygote critical window
- Added blkio tuning from sunfish
- Imported userdata tuning from oriole
- Set GPU idle timeout to 58 ms
- And alot more stuff on kernel side...

# 17-Nov-2022
- Initial Official build
- Fixed BT ldac
- Merged 4.19.265
- Updated dolby permissions

# 20-Jun-2022
- Own LOS 19.1 trees
- Update Immensity Kernel 4.0.0
- Update vendor to MIUI 13.0.6
- Update HALs to latest CAF/Codelinaro tags
- Some other fixes

# 09-May-2022
- New rebased trees from PPUI as base
- Change to Immensity Kernel 3.0.0
- Update vendor to MIUI 13.0.3
- Update HALs to latest CAF/Codelinaro tags
- Updated Adreno and Vulkan drivers
- Switch to new alioth audio source (clean import)
- Added Qualcomm TrueWireless Stereo
- Some other fixes

# 27-Apr-2022
- Update PowerProfiles to Android 12.1
- Update to last N0kernel Beta
- Update corner radius from stock 
- Align side fps ripple animation 
- Fix Video Calling 
- Some QTI Bluetooth fixes and improvements
- Fix Mifare nfc
- Fix AOD animation with Deep sleep
- New High Polling Rate implementation (source side)
- Implemented LiveDisplay and HBM
- Ram improvements

# 09-Apr-2022
- Rebased LOS 19.1 trees
- Change to n0kernel
- Updated vendor to MIUI 13.0.2
- Audio configurations from MIUI 13
- AOD auto brightness 
- Improved thermal profiles and refresh rate per app listview
- QTI Bluetooth
- Deep sleep on AOD
- Implemented Smooth Display

# 14-Mar-2022
- Change to new trees (base LOS)
- Change to Arrow Kernel
- Doze settings
- HOS Display calibration and HDR props
- Thermal profiles and QS Tile
- Clear speaker
- Refresh rate QS Tile
- More optimizations

# 11-Feb-2022
- Improved night display temperature
- Implement quicktap
- Fix statusbar burn in protection
- Improved ui smoothness
- Some audio changes
- Implement IORap
- ART optimization
- Imported rounded corners overlays from gourami
- And more fixes and improvements under the hood

# 16-Jan-2022 
- Updated Optimus kernel to v11.32
- Show refresh rate controls
- Fixed error alioth,aliothin using prebuilt recovery
- Align fp indicator with power button
- Display correct charging speed
- Allow all filesystems for USB-OTG
- WiFi improvements
- Audio improvements
- Imported some blobs and config from MIUI 13
