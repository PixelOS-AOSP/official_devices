# 22-Jul-2023
- Configure aux cameras for Aperture
- Face unlock now works fine (In the last update PixelOS switched to AOSPA's face unlock implementation, ParanoidSense)
- Fix Widevine/Netflix (Thanks @Linux4)
- Remove camera ID 51 from beyond2lte/beyondx (This ID refers to the device's second front camera, and this was causing problems with facial recognition for banks like C6 Bank)
- Set rounded corners and rounded mask (To make the recents, lockscreen, predictive gestures and others fit perfectly with the corners of the device and not look pointlessly square)
- Set status bar padding (for align with notch and make it look like stock)
- Update kernel to Linux 4.14.320

# 23-Apr-2023
- Compile the kernel without GCC
- Replace libutils-v32 with a shim
- Update blobs from *HWA1/*HWA3
- Update kernel to Linux 4.14.310
- Use linaro BSP

# 23-Feb-2023
- Fix NFC
- Revert SkiaGL stuff (causes lags)
- Disable blur for now (causes lags)

# 22-Feb-2023
- Add manually missing apn configs (4G/LTE and SMS fixed)
- Disable VSync for CPU rendered apps
- Enable zygote critical window 
- Switch to SkiaGL as HWUI renderer
- Update kernel to Linux 4.14.305
- Initial official release

