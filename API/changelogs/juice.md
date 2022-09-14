# 14-Sept-2022
- Fixed Fingerprint missing

# 11-Sept-2022
- Initial Android 13 build
- Switch to RRO Overlays
- Tune Ram Management from CAF/CLO
- Update Netflix BSP Property
- Import missing blobs for DRM
- Added Google Battery HAL

# 13-Aug-2022
- Rebased Trees
- Revert back into stock adreno stack
- With F2FS Compression
- Enabled FBEv2 Encryption


# 09-Jul-2022
- Add OpenGL ES and update Vulkan dEQP feature flags
- Build display composer from source
- Dropped libperfmgr
- Fixed mi_thermald not triggered at some time
- Flatten APEXs for performance
- Improvement sepolicy
- Improvement RAM management
- Switch to schedutil governor
- Update blobs from miui_LIMEPRE_22.6.22_b06e3696da_12.0
- Update display stack from nio S1RN32.19
- Update graphics stack from from LA.UM.9.14.r1-19300.01-LAHAINA.QSSI12.0
- Upstreamed kernel into latest
- Use audio policy volumes from AOSP

# 18-Jun-2022
- Initial release with OSS based
- Update blobs from miui_LIME_22.5.18_024e3361db_11.0
- Switch to Pixel Power HAL
- Import powerhint json from coral
- Tune powerhint json for our device
- Imported MIUI offline charging animation
- Set max WFD resolution to 1080p
- Sync idle/touch timer to raven
- Sync durations props with redbull
- Enable IORap app launch prefetching
- and many more

# 08-May-2022
- Fixed PixelOS Recovery
- Imported MIUI offline charging animation
- Set fingerprint/power button position
- Disable global mode and CDMA choices
- Fix deprecated power profile items
- Adjust padding between signal and battery icons
- msm_irqbalance: Correct the arch_mem_timer interrupt
- msm_irqbalance: Do not balance msm_drm and kgsl-3d0 IRQs
- Workaround device props based on SKU
- Add dalvik heap configuration for 4 & 6GB RAM
- Override verified boot state to green
- Disable OEM unlock
- Use surfaceflinger offset from crosshatch
- Reworked brightness
- Upstreamed kernel into latest

# 10-April-2022
- Initial Android 12.1 Official build release
- Improved I/O read-write speed
- Set max frame buffer to 3
- Re-enabled window-level blurs
- Disable VSync for CPU rendered apps
- Enforce 24-bit audio for offload playback
- Fixed video calling
- Disable forced shutter sound
- Tune ZRAM configuration
- Import sunfish cpusets configuration
- Import sunfish phase offset configuration
- Fixed Google TTS FC in Setup Wizard
- Decrease media volume steps
- Fully use RRO overlays (override vendor ones)
- Reworked statusbar padding and cutout
