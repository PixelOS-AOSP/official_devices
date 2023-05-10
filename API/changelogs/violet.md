# 10-May-2023
- Updated kernel
- Enable 24-bit for primary output and deep buffer
- Enable VoLTE/ViLTE/VoWiFi for entire 470 mcc

# 14-Apr-2023
- Upstreamed kernel
- Improved signal reception
- Boosted performance during bootup
- Enabled LTE_CA workaround
- Fixed issues with loud speaker
- Fixed random mic issues
- Redefined bluetooth a2dp offload capabilities

# 17-Feb-2023
- Fix low mic volume on VoIP
- Update device that aptX is pulled from
- Enabled audio suspend(reduces CPU/Battery usage)
- Disabled statusbar burn in protection(It was on by default in source)

# 22-Jan-2023
- Switched to Xcalibur kernel
- Removed ANX Camera
- Tuned vibration pattern
- Enabled call recording
- Added two channels for echo reference (reduces echo in calls)
- Redesigned FPS info 
- Increased statusbar padding
- Many under-the-hood changes

# 24-Nov-2022
- Switched to Litten kernel
- Fixed ram management
- Improved idle battery drain
- Added more dirac presets
- Many under the hood changes

# 21-Oct-2022
 - Removed Google Camera Go
 - Added ANX Camera(Portrait and 48mp won't work)
 - Updated kernel
 - Update system blobs from LA.QSSI.13.0.r1-05800-qssi.0
 - Lot of under the hood changes

# 14-Sept-2022
 - Initial A13 build

# 14-Aug-2022
- Updated blobs
 - Fixed videoplack issues on many apps
 - Added stereo config channel support to usb surround sound
 - Fixed mic issues on apps like WhatsApp
 - Added Bluetooth audio HAL for hearing aid
 - Switch to SkiaGL
 - Fixed cam interface on vilte calls
 - Fixed raise to wake icon on dark mode
 - Many under the hood changes

# 08-July-2022
 - Set ZRAM size to 50%
 - Increased systemimage partition size
 - Set max_comp_streams to 4 

# 10-June-2022
 - June security patch
 - Updated azure kernel to latest version
 - Fix low mic volume on voip
 - Disable stereo speaker in voicecall
 - Update charging voltage properties to R
 - Increased in-call earpiece volume
 - Deacrease launch boost to 3 sec

# 09-April-2022
 - Initial stable build based on Android 12.1
 - Entirely rebased trees
 - Updated azure kernel to latest version
