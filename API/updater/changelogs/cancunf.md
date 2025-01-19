\- Add complete support for moto g64 and moto g64y. 
\- FeLiCa Payment support added for Japanese units.
\- Fine Tune LMK and VM parameters.
\- Set proper dalvik heap properties for 4/8/12gb RAM units.
\- Update to proper CPUFreq Nodes on powerhint.
\- Drop redundant panel modules and firmware.
\- Implement VolumeSyncronizer for reducing the audio distortion at high volume.
\- Switch to custom 2.1 sensors MultiHal.
\- Skip loading Motorola's double/single tap sensors to prevent event keys from being blocked.
\- Implement PoweHAL Double Tap To Wake on NVT and ILITEK.
\- Implement Lineage Touch HAL.
\- Implement TapGestures from YAAP OP7 for single tap gestures on NVT and ILITEK.
\- Set show ambient as the default single tap gesture to match stock behavior.
\- Switch to schedutil as the cpufreq governor at boot and configure rate limits.
\- Drop fpsgo modifications from powerhint.
\- Drop MediaTek scheduler modules.
\- Include recovery ramdisk in vendor_boot to follow AOSP specifications.
\- Switch to DragonHeart kernel.
\- Kernel state at r1b2.
\- Implement support for WPA3-SAE enumeration.

Learn more at [blog.pixelos.net](https://blog.pixelos.net/)