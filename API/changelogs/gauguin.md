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
