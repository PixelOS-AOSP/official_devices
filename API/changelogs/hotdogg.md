# 17-Aug-2022
- Fix offline charging.

# 15-Aug-2022
- Commonize auto brightness configs.
- Ignore CNE in location indicator.
- Optimized auto brightness adjustment.
- Import night display color temp calibration from coral.
- Tweak msm_irqbalance.
- Uprev to multi-hal sensor 2.1.
- Configure vbswap instead of zram. (you can only stick with dragonheart).
- Set is_inline to 1 to kill UserLand Worker in inline builds.
- Set FP HAL thread to high CFS priority and use SCHED_RR for low latency.
- Kernel state at r16b3 (changelog at: here).

# 29-July-2022

- Initial Android 12 release.
- Bringup new tree from YAAP hotdog.
- Working 5G/NR.
- Working WiFi.
- June vendor SPL.
- EROFS is used for /system, /system_ext, /product, /odm and /vendor.
- F2FS for /userdata in conjunction with F2FS Compression which uses LZ4 as its compression algorithm.
- Updated relevant blobs from OOS 11.0.6.1.
- Build OnePlus Gallery.
- Add Tri-state UI overlay for alert slider.
- Add Screen-Off FOD overlay for screen-off FOD.
- Adapt status bar height to QPR3.
- Update graphics and adreno blobs from lahaina 19300.
- Switch back to opengl.
- Limit AOD & Ambient Display refresh rate to 60Hz.
- Use vibration patterns from OOS11.
- Limit AOD & Ambient Display refresh rate to 60Hz.
- Build Graphene Camera.
- Enable FUSE Passthrough.
- Build KProfiles Frontend.
- Nuke QTI WFD.
- LZ4 compression for ramdisk.
- Flatten Apex and use EROFS for it.
- Build with DragonHeart Kernel, GCC 12.1.0 and linked with LLD 15.0.0.
