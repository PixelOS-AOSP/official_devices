# 13 November 2023
- Initial Android 14 release

# 01-Oct-2023
- Bring back dropped media and audio configs [Temporary].
- Disabled APEX Compression in order to fix kernel panics.
- Drop Xiaomi CIT censor service because of no debatable improvements seen in ALS correction.
- Probing of NQ-NCI driver has been stopped when the HWC prop is detected as INDIA.

# 09-Sep-2023
- Resolved issue preventing users from flashing custom kernels in PixelOS recovery.
- Addressed problem hindering device shutdown.
- Restored max readahead size to 128KB.
- Rectified Power Off Charging anomaly.

# 05-Aug-2023
- Rebased kernel on CodeLinaro tag LA.UM.9.12.r1-15500-SMxx50.QSSI13.0.
- Merged ACK tag ASB-2023-07-05_4.19-stable.
- Massive cleanup of Xiaomi display driver changes.
- Drop unused media and audio configs.
- Utilize Xiaomi CIT sensor service for proper and smooth auto brightness transitions.
- Updated blobs to MIUI V14.0.3.0.SJSINXM.
- Switch to Pixel-like DCVS configuration.
- Massive cleanup of unwanted init scripts.
- Migrate to Xiaomi libperfmgr.
- Drop FM configuration completely.

# 21-Feb-2023
- Fixed Safetynet Attestation.

# 20-Feb-2023
- Rebased kernel
- Fixed USB tethering
- Enabled F2FS Compression
- Update adreno blobs from LA.UM.9.14.r1-20200-LAHAINA.QSSI13.0 
- Introduce Aperture
- Switched to common QTI vibrator HAL
- Update blobs from gauguin_GLOBAL_V13.0.7.0.SJSMIXM

# 19-Nov-2022
- Updated blobs from gauguin_GLOBAL V13.0.5.0.SJSMIXM release-keys.
- Updated specific camera blobs from gauguin_CN V13.0.10.0.SJSCNXM release-keys.
- Updated perf blobs from LA.UM.9.12.r1-14400-SMxx50.QSSI12.0.
- Drop OEM changes in gps.conf.
- Drop useless overlays.
- Drop IOP.
- Disable SF client composition cache.
- Fixed AOSP USB v2 audio HAL.
- Recovery is now made permissive.
- Switched to legacy sepolicy_vndr.
- Switched to common Xiaomi light HAL.
- Bump vendor security patch level.
- Update device build fingerprints.

# 02-Nov-2022
- Added support for MIUICamera
- Use AOSP USB v2 audio HAL

# 30-Oct-2022
- Dropped hw_acc effect from audio configs
- Add back LTM display configs
- Switch to AOSP NXP NFC HAL
- Suppressed warnings related to NeuralNetwork HAL
- Label missing wakeup nodes

# 27-Oct-2022
- Initial Android 13 Release

# 26-Jul-2022
- Drop KProfiles

# 16-July-2022
- Enabled F2FS Compression
- Introduced Raise to Wake
- Properly implement FUSE passthrough
- Introduced Thermal Profiles
- Refresh Rate QS Tile redirecting to it's own respective settings
- Addressed sepolicy denials
- Maybe fixed WeChat fingerprint issue

# 18-June-2022
- Add back MiSound Scenarios
- Drop atrace HIDL

# 14-June-2022
- Fixed PIP in apps like Netflix
- Fixed Quick Charging acting unusual
- Dropped Thermal Profiles
- Dropped MiSound Scenarios
- Dropped QS RefreshRate

# 12-June-2022
- Initial Release
