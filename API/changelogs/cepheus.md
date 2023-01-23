# 23-Jan-2023
- Added MIUI Camera
- Addressed more SELinux policy denials
- Drop pixel thermal hal workaround
- Drop s2idle usage
- Media: Update from LA.UM.9.1.r1-13000-SMxxx0.QSSI13.0
- Merge tag LA.UM.9.1.r1-13000-SMxxx0.QSSI13.0
- Move to lz4 for EROFS
- overlay: Add dummy udfps sensor (Fixes screen off fod toggle)
- Removed Dirac
- Switch back to OpenGL renderer
- Update CarrierConfig from LA.QSSI.13.0.r1-07400-qssi.0
- Update GPS blobs from LA.UM.9.1.r1-11500.02-SMxxx0.QSSI12.0
- Upstreamed kernel to 4.14.303
- Misc changes and improvements.

# 16-Nov-2022
- Switch back to SkiaGL renderer
- Sync brightness overlays with coral
- Switch to legacy sepolicy_vndr
- Some rootdir changes
- Powerhal related sepolicy changes
- Remove blur support
- Upstreamed kernel to 4.14.299
- Misc. changes & improvements

# 03-Nov-2022
- Fix memory management issues
- Fix AntiFlicker
- Fix screen off Ok Google
- Fix AAC and LDAC codec not working properly
- Address Pixel power libperfmgr HAL denials  
- Drop SkiaGL renderer 
- Update CarrierConfig from munch V13.0.4.0.SLMMIXM
- Include GrapheneCamera
- EROFS: Switch to lz4
- Add NoCutOutOverlay
- Upstreamed kernel to 4.14.296 and partially synced with SOVIET-ANDROID latest changes

# 21-Oct-2022
- Initial Android 13 build

# 12-Aug-2022
- Initial Official Build
- Fix DT2W
- Add IR blaster support
- Import gpio keylayout needed for AI button
- Disable Adaptive Connectivity preference
- Add LiveDisplay 2.1 (Antiflicker and Sun Light Enhancement)
- powerhint: Decrease launch boost to 3sec
- overlay: Fix Fingerprint Wake-up Animation
- wifi: set inactivity time
- overlay: Improve haptic and vibe patterns
- wifi: Smarter decisions on whether to use a 2 or 5Ghz AP
- Added props to improve scrolling and better responsiveness
- Disable client composition cache
- wifi: Enable QPower and Deep sleep at the same time
- kernel improvements for better responsiveness and idle drain.
- Add battery idle support for ACC
- Import and enable OPlus memory management hacks
- Various misc. changes
