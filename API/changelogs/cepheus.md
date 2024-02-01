# 01-Feb-2024
- Fixed stability and reboots when USB-C Type Headphones are connected
- Upstream kernel to 4.14.336
- Misc. improvements and fixes

# 25-Dec-2023
- Added back LiveDisplay support
- Added back charging control support
- Fix laggy video playback issue
- Fix UDFPS enroll radius
- Merge CLO tag 'LA.UM.9.1.r1-14900-SMxxx0.QSSI14.0'
- Upstream kernel to 4.14.334
- Misc. fixes and improvement

# 28-Nov-2023
- Added support for charging control
- Fix UDFPS enroll radius
- Upstream kernel to 4.14.330

# 13-Nov-2023
- Initial Android 14 release

# 31-Oct-2023
- Fixed GPS and heating issues
- Upstreamed kernel to 4.14.328

# 05-Oct-2023
- Update adreno from Moto G84
- Merge CLO tag LA.UM.9.1.r1-14200-SMxxx0.QSSI14.0
- Misc. improvements and fixes

# 22-Aug-2023
- Update task_profiles.json from AOSPA
- Update ueventd from LA.UM.9.1.r1-11500.02-SMxxx0.QSSI12.0
- Setup UClamp boosting
- Upstreamed kernel to 4.14.323
- Switch to TEO for cpuidle
- Misc. fixes and improvements

# 09-Jul-2023
- Change fingerprint color to white with red center
- Remove parts (clean speaker)
- Drop powersave governor
- Update Audio HIDL to 7.1
- Use foreground cpuset/uclamp for fingerprint
- Merge kernel CLO tag 'LA.UM.9.1.r1-13700-SMxxx0.QSSI13.0'
- Upstream kernel to 4.14.320
- Switch to Simple Low Memory Killer
- Misc. fixes and improvements

# 11-May-2023
- Switch FOD color back to green
- Set to powersave governor when device is idle
- Remove audio and Adaptive Battery CPU Throttling hints
- Make use of task_profiles and cgroups
- Fixed VoWiFi not working on outgoing calls or airplane mode
- Upstreamed kernel to 4.14.314
- Merged CLO tag 'LA.UM.9.1.r1-13500-SMxxx0.QSSI13.0' in kernel
- Backport f2fs from 6.4-rc1-5.10
- Silence more kernel logging
- Misc. fixes and improvements

# 16-Apr-2023
- Upstreamed to 4.14.312 
- Update cpusets for efficiency
- Update adreno to LA.UM.9.14.r1-21000-LAHAINA
- Switch to new UDFPS sensor implementation
- Update power_profile from coral
- Adjusted DC dimming values
- Dropped zram and use zswap+vbswap
- Fixed an issue with stuck scrolling through FOD area
- Fixed an issue with crashing calls on background
- Fixed brightness issues 
- Fixed deep sleep / idle drain
- Merged tag LA.UM.9.1.r1-13400-SMxxx0.QSSI12.0

# 23-Feb-2023
- Add power off alarm support (Needs LineageOS/DeskClock, or an alarm clock which supports power off alarm)
- Address more sepolicy denials
- Change default FOD pressed color to cyan
- Drop cpu affinity configs
- Enable qcrild and data services instead of starting them
- Inherit several Android Go configurations
- Switch to OSS mtdservice and mlipay
- Update telephony package list to LA.QSSI.12.0.r1-05600-qssi.0
- Silence CamX and CHIUSECASE log spam
- Switch to source built camera stack
- Temporary remove MIUI Camera due to reported issues
- Added Aperture camera with AUX support
- Use AOSP USB v2 audio HAL
- Add some missing IMS blobs
- Updated F2FS from Linux 6.2
- Merge CodeLinaro LA.UM.9.1.r1-13100-SMxxx0.QSSI13.0 tag
- Upstream kernel to 4.14.305 and compile it with playground clang 17

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
