# 11-May-2023
- Dropped PowerOffAlarm service which seemed to cause unwanted reboots
- Removed non-existent SF properties
- Switched to unsignaled buffer latching with AutoSingleLayer

# 08-May-2023
- Updated blobs from sweet V14.0.2.0.TKFMIXM
- Update mixer_paths_idp.xml from MIUI V14.0.2.0.TKFMIXM
- Disabled combined QS header
- Ignore CNE in location indicator
- Properly labelled fpc wakeup node 
- Cleaned up prebuilt display stack
- Disabled SF client composition cache
- Do not balance msm_drm and kgsl-3d0 IRQs
- Remove max ZRAM compression streams setting 
- Drop vestigial FM board-flags
- Upgrade IImsFactory to 1.1 in manifest
- Update QTI Radio LPA HIDL to 1.1
- Uprev bluetooth audio HIDL impl to 2.1
- Remove discard command tuning
- Don't mount TraceFS twice
- Upstreamed kernel to 4.14.314
- Merge CLO tag 'LA.UM.9.1.r1-13500-SMxxx0.QSSI13.0' in kernel

# 13-Apr-2023
- Updated blobs from sweet V14.0.1.0.TKFMIXM
- Repatched IMS from sweet V14.0.1.0.TKFMIXM
- Updated the s5kgw3 camera libraries from MIUI V14.0.1.0.TKFINXM
- Updated Adreno to LA.UM.9.14.r1-21000-LAHAINA.QSSI13.0
- Adjusted status bar padding 
- Fixed EGL symlink
- Updated XiaomiParts translations
- Updated VantomKernel

# 14-Feb-2023
- Updated blobs from sweet V14.0.1.0.TKFEUXM (Be sure to sure the updated firmware from the support group)
- Updated miuicamera from V14.0.1.0.TKFEUXM
- Added translations for XiaomiParts
- Adjust status bar padding once again (thanks Nayan)
- Kernel upstream, compiled with clang 17

# 02-Feb-2023
- Downgraded Adreno stack to older tag since a few games were crashing after the update
- Update blobs from sweet V13.0.16.0.SKFMIXM
- Fixed HDR in Netflix (using sweet's model this time)
- Fixed an issue with WiFi on the previous build
- Dropped LN8000 and Dolby

# 29-Jan-2023
- Update blobs from MIUI V13.0.15.0.SKFMIXM
- Update the s5kgw3 camera libraries from MIUI V13.0.9.0.SKFINXM
- Update the Adreno stack
- Added Motorola Dolby
- Uprev IQtiRadio with v2.6
- Uprev ImsRadio version to 1.7
- Uprev Bluetooth Audio HIDL to 2.1
- Uprev IFactory version to 2.3.
- Update GPS to LA.UM.9.1.r1-13000-SMxxx0.QSSI13.0
- Revert gps PROXY_APP_PACKAGE_NAME OEM change
- Improved adaptive refresh rate
- Disable SF composition prediction model
- Force device to treat 170M as sRGB in SF
- Disable redir_party_num
- ViLTE should work now?
- Tons of other misc. changes

# 25-Nov-2022
- Rebased on the latest xiaomi-sm6150 sources
- Included Sevtinge's modded Leica MIUICamera app
- Switched to an adaptive refresh-rate implementation
- Updated blobs from sweet V13.0.16.0.SKFEUXM
- Updated the s5kgw3 camera libraries from MIUI V13.0.7.0.SKFINXM 
- Updated XiaomiParts from lisa
- Updated power-libperfmgr
- Updated VantomKernel
- Various other misc. changes

# 21-Oct-2022
- Initial Android 13 release

# 12-Aug-2022
- Update blobs from sweet V13.0.12.0.SKFMIXM
- Fixed some RAM-related issues
- Fixed an issue with the headphones volume controls not working with wired headsets
- Fixed Fingerprint Wake-up Animation
- Fixed an issue where the quick settings would lag for some people while pulling it down
- Few changes regarding vibration
- Upstreamed kernel to 4.14.290
- Fixed an issue with the phone not being able to go to sleep due to smp2p_sleepstate
- Fixed some freezes
- Merged CLO tag LA.UM.9.1.r1-12100.01-SMxxx0.QSSI13.0
- Various other misc. changes

# 18-July-2022
- Always on Display and Ambient Display will now run at 60hz
- Fixed an issue with the microphone being too quiet in some apps
- Fixed an issue where the google recorder didn't want to work for some users
- Import new display calibration file from MIUI V13.0.10.0.SKFEUXM
- Update the s5kgw3 camera libraries from MIUI V13.0.5.0.SKFINXM
- Imported a few missing display blobs 
- Address Xiaomi's displayfeature & citsensorservice denials
- Enable 24-bit audio for primary output and deep buffer
- Added high touch polling rate
- Disabled IORAP
- Updated the adreno stack
- Possibly fixed some issues with smp2p-sleepstate
- Disabled CFI due to causing issues regarding performance 
- Upstreamed kernel to 4.14.288
- Other improvements and changes

# 12-July-2022
- Rebased on the latest xiaomi-sm6150 sources
- Switched to QTI bluetooth
- Fixed deep sleep on always on display
- Fixed an issue where AI mode caused CPU 6 to be stuck on maximum frequency
- Fixed PixelOS recovery not being able to flash stuff like Magisk
- Fixed a few issues with the microphone (R.I.P. Dolby)
- Labeled new wake-up nodes
- Some sepolicy fixes
- Upstreamed kernel to 4.14.287
- Enabled Ultra Low Power State Mode on suspend
- Other misc. changes and fixes

# 26-June-2022
- Switched to user builds
- Updated blobs from miui_SWEETEEAGlobal_V13.0.10.0.SKFEUXM
- Added support for JAPAN region (M2101K6R)
- Added back thermal profiles
- Added Neural Networks and Snapdragon Computer Vision Engine stack
- Updated media configs
- Fixed the always on display flicker
- Fixed camera interface on ViLTE calls
- Fixed a few issues with the microphone
- Labeled more wakeup nodes
- Switch SchedTune to UClamp
- Updated VantomKernel
- Other misc. changes and fixes

# 09-June-2022
- Updated blobs from MIUI V13.0.8.0.SKFMIXM
- Update adreno from LA.UM.9.1.r1-11500.02-SMxxx0
- Switched to EROFS (Enhanced read only file system)
- Enabled F2FS compression (Needs a clean flash to work)
- Added Moto Dolby with a tuned configuration from MIUI on the Redmi Note 10 Pro (Thanks helenius147)
- Optimize native executables for Cortex-A76 CPU
- Switch to dot product CPU variant
- Improved vibrations
- Nuked Vulkan (due to some heating/drain)
- Fixed picture adjustment in LiveDisplay (Do NOT change kernel if you want LiveDisplay to function properly)
- Fixed the remaining stuff in miuicamera like clone mode (thanks to Adarsh) P.S. slow-mo is still dead
- Updated VantomKernel and PlayGround clang
- Other misc. changes

# 13-May-2022
- Initial miuicamera import from miui_SWEETEEAGlobal_V13.0.9.0.SKFEUXM
- Reintroduced HBM and anti flicker mode
- Fixed an issue where sometimes unlocking would get stuck on the lock screen clock
- Fixed the charging issues a few people had (disconnecting)
- Changes to power_profile.xml for better battery usage information and estimates
- Increased ZRAM to 3GB
- Improved memory management
- Labeled more wakeup nodes
- Resolved more denials
- Updated kernel and compiled using the latest playground clang
- More misc. changes and fixes

# 06-May-2022
- Updated blobs to V13.0.9.0.SKFEUXM
- Switched to Vulkan UI renderer
- Removed iorap due to (probably) causing some heating/drain
- Improved RAM management
- Labeled more wakeup nodes 
- Addressed more denials 
- Updated kernel

# 29-Apr-2022
- Removed HBM for now due to issues with brightness
- Updated vibration patterns 
- Updated deprecated screen power items 
- Fixed more issues with ANXCamera (Colors and details getting messed up)
- Added a few missing blobs
- Added MGLRU for better memory management
- Dropped SLMK in favor of LMKD
- Use LMKD from YAAP for better memory management
- Updated kernel
- Misc. changes and fixes

# 27-Apr-2022
- Updated blobs to MIUI V13.0.8.0.SKFEUXM
- Update GPS from LA.UM.9.1.r1-11800-SMxxx0.0
- Fixed aptX and aptX HD
- Fixed IR blaster 
- Fixed issues with the status bar
- Slightly increased the status bar height (to how it was on older builds)
- Fixed the document, panorama, vlog and long exposure modes in ANXCamera
- Fixed the ANXCamera crash in the full aspect ratio and the 64/108MP mode in sunlight 
- Fixed the blue/green tint some users had
- Fixed some more issues with camera
- Fixed the fingerprint wake-up animation
- Fixed the low-mic issues that some people had using a few apps
- Fixed WiFi Display (Miracast)
- Fixed some issues with dirac
- Introduced haptic control
- Improved vibrations 
- Introduced livedisplay
- Introduced doze modes 
- Updated VantomKernel compiled with playground clang 15 with optimizations
- Misc. fixes and changes

# 12-Apr-2022
- Switched to Arian's common tree
- Various fixes such as fixed work profile, vibrations
- Updated VantomKernel

# 12-Mar-2022
- Merged latest linux-stable v4.14.271
- Merged latest CAF tag LA.UM.9.1.r1-11700-SMxxx0.0
- Updated blobs from MIUI V13.0.4.0.SKFMIXM
- Reverted Vulkan changes (Should fix some GCams not working and a few frame drops)
- Fixed the front camera cutout protection
- Added the saturated color mode
- Enabled combined signal icons in the status bar
- Enabled auto brightness for Ambient display
- Set SOC manufacturer and chipset properties 
- Improved fingerprint animation when you unlock the device
- Improved app launch speeds
- Improved vibrations

# 15-Feb-2022
- Switched to Vulkan UI renderer
- A few more Dirac fixes
- Enable support for Bluetooth hearing aids
- Thermal settings's app list improvement
- Updated media volume steps
- Removed updateable apex
- Upstreamed kernel to v4.14.266
- Other misc. changes

# 11-Feb-2022
- Upstreamed kernel to v4.14.265
- Merge CAF tag LA.UM.9.1.r1-11600-SMxxx0.0
- Update blobs from sweet-qssi-user-12-RKQ1.210614.002-V13.0.2.0.SKFMIXM-release-keys
- Changed the default camera app from snap to ANXCamera v204
- Allow screen to be rotated in all 4 rotations.
- Enabled IORAP feature to improve the application launch time.
- Increased vibration pattern
- Added clear speaker
- Fixed "OK Google"
- Fixed Dirac
- Enabled Quick-Tap
- Enabled the pre-rendering feature
- Disabled RX wakelock feature
- Fingerprint animation unlock ripple is now to the right side instead of the center
- Screen now turns on when plugged/unplugged
- Apps like YouTube, Netflix etc switch to 60hz when minimum refresh rate is set to 60hz.
- Adjust screenshot chip dimensions
- Follow monet color in icon
