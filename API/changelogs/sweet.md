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
