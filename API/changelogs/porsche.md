# 17-Jan-2024
- test

# 16-Jan-2024
- Brought back LiveDisplay
- Set default hotspot ssid
- Misc. changes

# 27-Nov-2023
- Initial build based on Android 14

# 14-Sep-2023
- Updated device specific blobs to RUI 13.1.0.1411
- Fixed mic related issues in calls and games
- Updated Adreno/Graphics blobs to LA.UM.9.14.1.r1-10300-QCM6490.QSSI13.0 (V600)
- Ditched OplusGallery and patched OplusCamera to use GPhotos as default gallery
- Fixed camera viewfinder layout
- Latest RUI 13.1.0.1411 firmware included
- Lots of kernel side improvements

# 29-Jul-2023
- Updated device blobs from RealmeUI 4.0 C.15 (EX01)
- Fixed battery drain
- Fixed heating
- Improved app launch speeds 
- Improved Dolby Atmos
- Fixed issues with Airtel network
- Latest RealmeUI 4.0 C15 firmware included

# 13-Jul-2023
- Updated blobs from Realme UI 4.0 C.14 (EX01)
- Updated display and bluetooth stack from LAHAINA 21000
- Switched to AIDL bluetooth audio service
- Improved aod
- Massively slowed down autobrightness ramp/decrease rates to fix occasional flickers
- Lots of kernel changes and improvements

# 14-May-2023
- Switched to user build
- Improved haptics effects
- Fixed USB-C analog earphones 
- Implemented aosp hbm replacing livedisplay sunlight mode
- Kernel upstreamed to v5.4.242
- Disabled a whole lot of debugging and logspam in kernel
- Switched to OSS display hal
- Updated display blobs from Sony Xperia 1 III and display postprocessing blobs from LAHAINA 20200
- Updated adreno graphics stack from LAHAINA 21000
- Update to audio HAL V7 
- Switch to aosp doze service for better lift to wake detection
- Updated thermal blobs to LAHAINA 20200
- Update IMS stack to QSSI 08600
- Enabled FUSE passthrough
- Limited AOD to 60hz
- Improved memory management

# 15-Apr-2023
- Initial Android 13 release