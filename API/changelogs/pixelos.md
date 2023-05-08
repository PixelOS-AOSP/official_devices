# 8-May-2023
- Merged the May security patch
- Switched back to the Pixel launcher (with a potential fix) and Pixel theme picker
- Brought back unlinked ringer streams
- Brought back the option to hide the power menu on the secure lock screen
- Added option for haptic feedback on back gesture
- Added button to upload crash log to Memocho for easier bug reporting
- Minor improvements to SafetyNet/banking app hiding
- Made App Lock more properly accessible and fixed a few issues
- Update pocket mode style to the latest OxygenOS specs
- Re-organized the sound settings
- Introduced the power-off-alarm service
- Updated themed icons
- HWUI improvements
- Reduced log spam
- Other improvements

# 13-Apr-2023
- The March/April patches have been merged
- Switched to the Paranoid Android Launcher
- Added icon styles and icon shape options
- Added ability to switch fonts
- Added over the air updates
- Added AppLock
- Use Monet colors for the power menu 
- Updated the Bluetooth tile implementation
- Updates to the network traffic indicator implementation
- Updates to the Dark Mode implementation

# 14-Feb-2023
- The February patch has been merged
- Switch to PropImitationHooks
- Updated GMS components from the Pixel 5 (redfin)
- CTS/Play Integrity passes again
- Switched Network Traffic implementation
- Switch to Immersive Navigation
- Added Volume Long Press Skip Tracks
- Allow hiding power menu on secure lockscreen
- Require unlocking to use sensitive QS tiles
- Allow disabling screenshot shutter sound
- Introduce camera & flashlight keyguard affordance
- Allow setting bottom keyguard shortcuts

# 26-Jan-2023
- Rebased on android_13.0.0_r20
- Switched to tracking most repositories from LineageOS
- Switched to Aperture as the default camera app
- Improved smooth display implementation for devices with higher refresh rates
- Updated GMS components from the latest Pixel release
- Added Network speed indicator for monitoring internet connection
- Added an option to show data usage in the quick settings
- Added one-shot auto brightness
- Added configurable rotation angles for auto-rotate
- Added an ADB root toggle
- Improved black (dark) mode
- Organized sound settings
- Bluetooth dialog tile is now optional, with both custom and stock options available
- Switched to the Expanded volume dialog implementation

# 16-Nov-2022
- Merged android_13.0.0_r14
- Use Google Sans systemwide
- Added bluetooth dialog
- Added face unlock
- Added optional haptic on back gesture
- Added one shot auto brightness
- Allow disabling refresh rate lowering in battery saver
- Add button to upload crash log to memocho
- Added Smart Pause feature
- Added navbar inversion turning
- Added optional Wi-Fi standard icons
- Fully switched to Pixel sounds
- Added black mode
- Moved dev refresh rate controls under display settings
- Organized sound settings
- Fixed call vibration settings not showing up on some devices
- UI/UX optimizations and Privacy improvements
- Minor UI/UX changes
- Updated translations

# 20-Oct-2022
- PixelOS Stable release based on Android 13

# 8-Sep-2022
- Initial PixelOS Beta release based on Android 13

# 12-Aug-2022
- Merged August Security Patch
- Introduced Quick unlock
- Added an option to scramble pin layout when unlocking
- Added an option to hide power menu on secure lockscreen
- Allow user configurable fingerprint wake and unlock
- Fixed an issue where vibration intensity would reset on some devices
- Fixed volume panel background color in light mode
- Restored default Pixel font behavior
- Enable strict standby policy
- Rework screen off FOD
- AppLock improvements
- Updated translations
- More miscellaneous changes and fixes

# 8-Jul-2022
- Merged July Security Patch (android-12.1.0_r11)
- Fixed issues with HDFC banking apps detecting root access
- Extended Applock support to various system apps
- Added optional Daily data usage in expanded quicksettings
- Updated per-app volume drawable to match other system elements 
- Improvements in statusbar icon paddings
- Added toggles for vibration icon and old style mobile data indicators in Icon manager
- Made battery & clock clickable again in quick statusbar header
- Updated translations (thanks to everyone who contributed).

# 17-Jun-2022
- Applock is now stable (exposed in security settings)
- Added support for per-app volume
- Added an option to remove the screenshots and screenrecords limits for all applications
- Fixed Media picker SystemUI crash
- Fixed widgets crash on PixelLauncher
- Fixed semi bold font on PixelLauncher
- Added material-you preview animation to  double tap to doze gesture
- Added Data Switch QS Tile
- Added delete action for screenshot and screenrecorder notifications
- Fixed colors on DocumentsUI
- Updated translations

# 9-Jun-2022
- Rebased source over PixelExperience
- Added Network Traffic Indicator
- Added App Lock (beta)
- Added support for one shot auto-brightness
- Added button to restart SystemUI in advanced reboot
- Added option to disable screenshot shutter
- Added user interface for Alert Sliders
- Added double tap to trigger doze 
- Added a button to upload crash log to memocho
- Added a toggle for combined signal icon
- Added a toggle for haptic feedback on back gesture 
- Added custom vibration patterns from OxygenOS
- Added vibration intensity control 
- Fixed issues with the quick settings page
- Fixed issues with the navigation bar while in landscape

# 6-May-2022
- Merged May Security Patch
- Added expanded volume panel
- Added quick settings tile for Auto brightness
- Updated the caffeine quick settings tile icon from AOSPA
- Update package details to match S style
- Fixed an issue where battery percentage would refresh while accessing app drawer on white theme
- Bunch of fixes in Updater app
- Miscellaneous changes and fixes

# 26-Apr-2022
- Added quick setting tiles for caffeine, heads up, sync, ambient display, Always on display, USB tether quick settings tiles, live display
- Fixed some issues with advanced reboot
- Added back charging animation
- Introduce high touch polling rate feature control
- Introduced live display
- Added Aggressive Idle mode under battery saver settings
- Allow toggling screen off FOD for supported devices 
- Allow option to disable screenshot shutter sound
- Move Force max refresh rate preference to display settings
- Allow to enable high refresh rate even when battery saver is on 
- Added a switch for linked ring and media notification volumes
- Allow disabling unlocking ripple animation
- Apply monet to fingerprint authentication ripple animation 
- Fixed issues with the camera in some apps like telegram for some devices
- Fixed an issue where unlock sound was played multiple times
- Fixed an issue where the hide pill option wasn't working for some people
- Fixed Separate QS tiles for WiFi and Mobile data
- Updated themed icons
- Reduced logging and silenced some log spam

# 9-Apr-2022
- Merged April Security Patch
- Added doubletap/longpress power to toggle torch
- Removed text from expanded screenshot chip
- Allow to disable battery estimates in QS
- Added bluetooth battery icon in status bar
- Introduced status bar tuner
- Introduced full screen display
- Allow hotspot to use VPN upstreams
- Added in-call vibration options
- Finetuned status bar padding and added alarm and vibrate icons
- Allow to disable privacy indicators
- Introduced Quick unlock
- Added immersive navigation
- Added separate QS tiles for WiFi and Mobile data
- Added navbar layout inversion 
- Rearranged and categorized gestures
- All themed icons are now vectorized
- Misc. fixes and optimizations

# 12-Mar-2022
- Merged 12.0.0_r32
- Added Face unlock
- Added App Lock
- Added per app network restriction permission
- Introduced Android 12L style Internet and Screenrecord dialogs
- Added Android 13 inspired Media Output Picker
- Added support for left side volume panel (for OnePlus devices).
- Added more themed icons 
- Switched back to the smooth display implementation of high refresh rate
- Upstreamed all the relevant repos with LineageOS
- A lot of bug fixes from PixelExperience
- Power draw and scrolling improvements
- Updated translations
- Misc. fixes and optimizations

# 11-Feb-2022
- Merged February security patch
- Added more themed icons 
- Added quicktap (for supported devices)
- OTA Updates for Official builds
- Added in-call vibration options
- Shipped PixelOS themed recovery
- First class implementation of repainter app
- Added Adaptive playback
- Fixed Pixel buds app for non pixel device 
- Fixed the issue where phone fails to switch from stereo to mono on some devices
- Added monet to Settings app icon color
- Fixed battery saver quick settings tile
- Added an option to disable unlock ripple animation 
- Performance improvements
- Updated translations
- Misc. fixes and optimizations

# 15-Jan-2022
- Merged android-12.0.0_r27
- Added HeadsUp QS tile
- Added Long press volume key to change track
- Fixed an issue where QS got bugged after unlocking device with fingerprint
- Added back delete action for screen recordings in QS notification
- Improved Scrolling Cache
- Added a button to restart SystemUI in advanced reboot
- Fixed DT2W summary in display settings
- Added sliders for color balance adjustment 
- Added missing icons in Network and Internet settings
- Added an option to open app directly from App info
- Added package name to installed app details
- Updated translations
- Bugfixes and misc. improvements

# 31-Dec-2021
- Fully rebased android-12.0_r18
- Spoofed as Pixel 1XL for google photos for unlimited backup in original quality
- Added themed icons for a lot of third party icons in stock PixelOS Launcher
- Added monet in power menu
- Exposed legacy WiFi and Cellular data QS tiles
- Added bluetooth battery level indicator on status bar
- Added NFC tile in QS for supported devices
- Added doubletap/longpress power button to toggle torch
- Adapt screenrecord dialog switches to Android 12
