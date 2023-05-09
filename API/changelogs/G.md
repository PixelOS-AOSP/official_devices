# 09-May-2023
- Enabled CA by default

# 14-Feb-2023
- Improved fingerprint unlock speed (same as a12 now)
- linkerconfig selinux spams are suppressed
- Enabled WPA3 support
- Fixed PowerOff Alarm (You will need DeskClock or alarm clock which supports poweroff alarm)
- Cleaned up adsp blobs
- Cleaned up audio blobs
- Cleaned up CNE blobs
- Cleaned up DRM blobs
- Cleaned up Graphics blobs
- Cleaned up Media blobs
- Cleaned up Radio blobs
- Cleaned up IMS blobs
- Cleaned up GPS blobs
- Forcefully disabled statusbar burn-in protection
- Removed RenderScript
- Setup all the sub-system as related
- Dropped FDE leftovers
- 10or --> 10.or
- Disabled bluetooth enhanced SCO connection
- Inherited 2048 dalvik config as fallback for GSIs
- Dropped trusted user interface 
- Dropped unused OMX codecs 
- Made fingerprint HIDL fully treble compliant 
- Fixed non-ASCII character in gps.conf
- Dropped 3.18 kernel support from fstab
- Fixed ims sylink as per retrofit dynamic partition
- Updated CNE, QMI, RADIO, IMS from FP3
- Kanged DPM again from Nokia Panther

# 24-Jan-2023
- Initial stable release based on Android 13
