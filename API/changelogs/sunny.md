# 25-May-2025
- Update libnotifyaudiohal from ruby V816.0.5.0.UMOMIXM to resolve an issue where the proximity sensor wasn't working.

# 17-May-2025
- Switch to common hardware/xiaomi VINTF fragments.
- Switch to common AIDL lineage fingerprint HAL.
- Drop unused lights HAL.
- Switch to common device compatibility matrix from QCOM.
- Resolve warnings in the GPS HAL.
- Convert GPS HAL to blueprint.
- Migrate mountpoint creation to blueprint.
- Shim widevine libs with libcrypto_shim.
- Switch to python extract-utils.
- Enable and resolve ELF checks.
- Clean up system IMS stack.
- Drop prebuilt com.fingerprints.extension@1.0 as we are building the reversed implementation from hardware/xiaomi.
- Drop media component and switch back to stock media blobs.
- Clean up media stack.
- Drop OMX completely and switch to Codec2.
- Drop all BUILD_BROKEN flags.
- Fixed an issue where in-call voice breaks when notification arrives.
- Upgrade audio HAL to v7.0.
- Drop first_stage_ramdisk GSI keys as it is redundant.
- Enable Userfaultfd GC to improve memory management. (should improve the experience on 4GB RAM variants)
- Upgrade tetheroffload HAL to 1.1.
- Switch back to prebuilt camera provider to retain camera and flash capabilities on devices where one or more lenses are broken.
- Kernel state at r17b13.

# 17-Feb-2025
- Implement adjustable strength flashlight support.

# 17-Jan-2025
- Fixed an issue where VOIP routing is misconfigured.

# 16-Dec-2024
- Properly disable turbulence effect to fix QS lags on media player.
- Switch to AIDL Fingerprint HAL to fix fingerprint icon indicator position.
- Kernel state at r17b12.
