# 24-Feb-2026
- Patch some blobs to depend on libtinyxml-v34.so.
- Set group key for display settings IA on DisplayFeatures.
- Set group key for battery settings IA on KProfiles.

# 28-Jan-2026
- Drop legacy platform hacks for BPF.
- Override kernel BPF version to 5.4.299.
- Drop init.is_legacy_ebpf cmdline prop as it is unneeded anymore.
- Fixed an issue where the updater app crashed upon trying to OTA / local install.
- Kernel state at r18a2.

# 15-Jan-2026
- Disable blurs by default.

# 20-Dec-2025
- Move back to QTI PerfD HIDL stack as the AIDL stack causes an abundance of logspams.
- DisplayFeatures: Specify export behavior for BroadcastReceiver.
- DisplayFeatures: Implement CABC mode to be utilized on devices that support it.
- DisplayFeatures: Remove preferences of toggles that are unsupported.
- DisplayFeatures: Reword summary of DisplayFeatures.
- DisplayFeatures: Check if tiles are started first to unregister.
- DisplayFeatures: Only restore preferences if they are available.
- DisplayFeatures: Completely hide unavailable QS tiles.
- DisplayFeatures: Store CABC value in SharedPreferences and restore at boot.
- DisplayFeatures: Don't restore HBM at boot as it is a bad practice.
- DisplayFeatures: Add French and Spanish translations.
- DisplayFeatures: Protect FpsService broadcast.
- DisplayFeatures: Protect AFMScheduleService broadcast.
- DisplayFeatures: Minor improvements.
- Update horizontal keyboard placement props to better match our device.
- Disable data roaming by default.
- Drop qcom/common entirely and switch back to stock GPU stack.
- Enable blurs.
- Fine tune status bar paddings.
- Refine display cutout.
- Disable high performance blur transitions.
- Drop debug.sf.disable_client_composition_cache as it causes visible jank.
- Reduce blur radius in systemui and launcher.
- Opt out of speaker_layout_channel_mask field to fix an issue where there is no incoming call ring tone on bluetooth/headset.
- Kernel state at r17b15.

