# 12-Aug-2022
- Disable ALAC support 
- Use default allocstall threshold on k4.9 
- Tune zram & swappinness 
- Correct console config property 
- Unset config_lockscreenAntiFalsingClassifierEnabled 
- Re-enable rounded corners 
- Dirac: cleanup & refactor code 
- fix zygote preforking prop 
- fix deprecated power profile items 
- Added prop for smoother scrolling and better responsiveness 
- Clear settings cache after dirty flash 
- enable Multiuser Overlay 
- Update OK Google from OnePlus 9 Pro

# 17-July-2022
- IMS: Add whitelisted broadcast
- Update gps config from LA.UM.10.6.2.r1-02200-89xx.0
- Update Display HAL from LA.UM.10.6.2.r1-01900-89xx.0
- Upstream kernel from LA.UM.10.6.2.r1-02200-89xx.0

# 18-June-2022
- Upstreamed kernel to 4.9.319
- Synced with latesy CAF tags as of 18 June 2022

# 10-June-2022
- Set permissions for KGSL sysfs node
- Increase BootCompletedReceiver priority (Helps to restore parts changes as soon as device boots up)
- Enable the pre-rendering feature
- Optimise dex flags
- Commonize vibrator pattern values (vibration pattern has been changed on trial basis, If you dont link inform me in support group, I will remove it in next build)
- Uprev clearkey DRM HIDL to 1.4
- Added Advanced Control
- Upstream kernel from LA.UM.10.6.2.r1-01900-89xx.0
- Upstream kernel to 4.9.317

# 9-May-2022
- Update media config from LA.UM.10.6.2.r1-01100-89xx.0
- Dual sim should work
- Vilte should work
- Shorten wait time for services exit to optimize shutdown
- Uprev bluetooth audio HIDL impl to 2.1
- Remove obsolete eBPF property
- disable compressed APEX
- Enable discard option to retain speed
- Only compile 32-bit audio.primary.msm8953
- Fix duplicate sysprop assignment for rild.libpath
- Cleanup ril packages & drop tel. injection
- Remove IO read_ahead_kb tune
- Auto select Data/SMS/Voice preference in SIM hotswap
- Remove sensors specific boot up commands from init.qcom.rc
- msm8953_64 target specific changes for sensors
- Add OpenGL ES and update Vulkan dEQP feature flags
- Use threaded GLES render engine
- Add ro.hw_timeout_multiplier
- Build sound_trigger from source
- Remove vendor RenderScript implementation
- Don't manually set call vol steps
- Upstream kernel from LA.UM.9.6.2.c25-02800-89xx.0
- Upstream kernel to 4.9.312

# 13-March-2022
- Fixed mobile data on sim 2
- Upstreamed kernel to 4.9.304
- Added face unlock 
