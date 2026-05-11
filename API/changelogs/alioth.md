# 11-May-2026
- Increase swappiness to 100
- Clean up init scripts
- Backport locking changes from k5.4 to improve performance
- Implement kmem_cache pooling for filesystem and driver modules to accelerate memory allocation
- Merge the latest changes from Lineage/qcom_8250

# 10-Apr-2026
- Upstream kernel zstd version
- zram: remove additional locking
- Merge the latest changes from LineageOS/qcom_sm8250

# 12-Mar-2026
- Source upstream

# 24-Feb-2026
- Fix I2C write failures in certain scenarios
- Fix WFD crash
- Fix performance issues with Samsung UFS
- Patch some blobs to depend on libtinyxml2-v34
- Move parts to the system category
- Reduce touch response latency under high load
- Define OEM fast charge sysfs node

# 18-Jan-2026
- Fixes the issue of not receiving ringtones when using headphones.
- Upstream LZ4 to 1.10
- Add back OMX
- Enable percpu high priority kthreads for erofs

# 23-Dec-2025
- Initial A16 release
- Redo brightness configuration
- Add support for HDR/SDR mixed display
- Drop debug.sf.disable_client_composition_cache prop
- Fixes random reboot issue caused by incomplete BPF backport.
- Cleanup more flags

