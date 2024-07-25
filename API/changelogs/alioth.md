# 25-Jul-2024
- Added dolby support
- Dropped KProfiles
- Disabled volume leveler
- Updated CarrierConfig from munch V816.0.2.0.ULMMIXM
- Updated patched ims from munch

# 28-May-2024
- Update blobs from munch HyperOS OS1.0.1.0.ULMMIXM
- Switch to common libqti-perfd-client and power-libperfmgr
- Enabled GAME power mode in power HAL
- Don't boost top-app on interaction

# 12-May-2024
- Brought back Leica camera
- Fixed 1440p, 4K and HDR videos
- Updated blobs from HyperOS OS1.0.2.0.TKHMIXM
- Source upstream

# 28-Apr-2024
- Kernel upstream
- Added TEO cpuidle governor
- Added SBalance with latest sultan changes
- Uprev audio hal to 7.0
- Debloated kernel
- Updated Display blobs to LA.UM.9.12.r1-15100-SMxx50.QSSI13.0
- Nuked leica (It's broken, Aperture present)

# 18-Feb-2024
- Merged latest ACK (4.19.306)
- Merged latest CLO tag (LA.UM.9.12.r1-18100-SMxx50.QSSI14.0)
- Switched to WFI only (should reduce the drain on deep sleep)
- Switched to 100hz tick rate (should decrease power consumption)
- Imported minimal Mi_thermald changes from AOSPA
- Implemented spatial audio from cheetah
- Dropped doze related features
- Added xiaomi cit sensor
- Removed unwanted dolby sepolicy
- Removed unwanted audio blobs

# 18-Jan-2024
- Source upstream 
- Kernel upstream
- Updated power profile from stock
- Adjusted statur bar padding
- Switched to vendor-defined color modes
- Added back 32 bit app support
- Fixed AOD black screens
- Disabled display refresh rate override
- Disabled a lot of debug configs on kernel side

# 22-Dec-2023
- Updated refresh rate timings from op9 PA
- Improved kernel scheduler
- Nuked teo cpu idle governor on kernel side (seems like it was draining a bit more)

# 28-Nov-2023
- Source Upstream
- Added charging control
- OTA is now faster due to Dexopt changes
- Kernel changes...

# 18-Nov-2023
- Fixed device Integrity (once again)
- Eliminated debug codes in QCA-CLD
- Built with Aosp Clang 17.0.4

# 12-Nov-2023
- Initial A14 beta release
- Merged 4.19.297 from ACK
- Fixed play device integrity
- Nuked Dolby

# 29-Oct-2023
- Implemented Dolby from Paranoid Android
- Fixed USB dac
- Updated Carrier Config from munch V14.0.3.0.TLMMIXM
- Enabled 5G SA and NSA
- Implemented charging control

# 15-Sep-2023
- Updated Adreno/Graphics blobs to LA.UM.9.14.1.r1-10300-QCM6490.QSSI13.0 (V600)
- Fixed lift to check phone
- Use the new auto network selection UI
- Decreased top-app schedtune boost to value 1
- Updated kprofiles to 6.0.0
- Decreased latency and heat on kernel side
- Override Aperture

# 15-Sep-2023
- Updated Adreno/Graphics blobs to LA.UM.9.14.1.r1-10300-QCM6490.QSSI13.0 (V600)
- Fixed lift to check phone
- Use the new auto network selection UI
- Decreased top-app schedtune boost to value 1
- Updated kprofiles to 6.0.0
- Decreased latency and heat on kernel side

# 21-Aug-2023
- Fixed random reboots (Caused by modem crashes)
- Updated blobs to V14.0.9.0.TKHEUXM
- Added FPS info qs tile
- Moved Thermal Profile to System
- Dropped LiveDisplay
- Reverted more color profiles (Was giving black screen issues)
And alot more...

# 18-Aug-2023
- Rebased Kernel over lineage
- Decreased top-app schedtune boost (Saves more power usage)
- Fixed Facebook marketplace (Source side)
- Added more color profiles
- Merge f2fs stable (Kernel Side)
- Enabled Optimized Power Management
- Optimized native executables for Cortex-A76 CPU
- Alot more changes on kernel side...

# 12-Jul-2023
- Fixed offline charging
- Enabled wallpaper zoom
- Tuned vibration patterns
- Improve performance when the main System UI thread is busy.
- Some kernel changes

# 06-Jul-2023
- Source upstream

# 05-Jul-2023
- Merged latest ACK (4.19.288)
- Merged latest clo tag (LA.UM.9.12.r1-15500-SMXX50.QSSI12.0)
- Improved deep sleep
- Disabled sf EGL image tracking
- Disabled cpu boost 
- Disabled msm performance (we are using libperfmgr its useless)
- Tuned Adaptive Suspend parameters
- Move background cpuset to CPU0-1 (Might save more power)

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
