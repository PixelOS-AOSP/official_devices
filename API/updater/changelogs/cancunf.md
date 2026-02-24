\- Update blobs to V1TD35M.83-20-5.  
\- Switch to AIDL imgtuner service.  
\- Add dav1d software video decoder.  
\- Update IMS patches to V1TD35M.83-20-5.  
\- Update blobs to V1TDS35M.83-20-5-3.  
\- Add permissions for com.android.nfc_extras and com.nxp.mifare.  
\- Switch to using phase offsets as durations for SurfaceFlinger to reduce jitter and improve vsync.  
\- Drop vsync event props as they are not to be utilized with phase durations.  
\- Unsignal buffer latching with AutoSingleLayer to reduce app jank while being unaffected by display freezes.  
\- Enable GL comp backpressure to avoid jank due to HWC queue stuffing.  
\- Update CarrierConfigOverlay to V1TDS35M.83-20-5-3.  
\- Reduce max resolution for HEIF images to prevent HW overload issue.  
\- Move kernel modules to a new DLKM vendor_ramdisk fragment to improve modularity.  
\- Drop mtk_perf_common module as we don't need it.  
\- Drop AEE and ATF modules as they are debugging modules.  
\- Enable ELF checks for libimsma.  
\- Drop BesLoudness as we don't need it.  
\- Add permissions for com.mediatek.ims.config.xml.  
\- Address more SEPolicy for wakeup nodes.  
\- Patch mtkfusionrild to load libutils-v32 to fix RIL.  
\- Switch to LZ4 compression for EROFS images to improve decompression speed substantially.  
\- Add WifiResOverlay for G64Y (XT2431-2).  
\- Ship full firmware within the ROM zip.  
\- Label SEPolicy for persist.moto.vt.timegap.  
\- Update VT system blobs from rothko A16 to fix VT.  
\- Update AVB rollback index from V1TDS35M.83-20-5-3.  
\- Install apex for clearkey service.  
\- Switch to regular AIDL Wi-Fi HAL over the lazy HAL as we don't need to defer initialization of Wi-Fi.  
\- Move to reference fastboot AIDL service.  
\- Cleanup Lights AIDL HAL.  

Learn more at [blog.pixelos.net](https://blog.pixelos.net/)