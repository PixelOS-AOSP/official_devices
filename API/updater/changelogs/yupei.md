\- Fix lag in the first back gesture animation when closing an app.  
\- Fix lowi-server crash looping in the background.  
\- Game mode:  
\  - Hold CPU and GPU frequency floors and keep all cores online while a game is running.  
\  - Switch to Xiaomi's game thermal profile so it doesn't throttle as early.  
\  - Raise vm.max_map_count for emulators like Winlator and GameHub.  
\  - Expose /dev/ntsync to apps for faster Wine sync on Windows emulators.  
\- Use 64K mTHP for app memory.  
\- Kernel:  
\  - Build with ThinLTO and AutoFDO.  
\  - Backport per-CPU page list auto-tuning from Linux 6.7.  
\  - Always use LSE atomic instructions.  
\  - Add the Xiaomi thermal interface.  
\  - Enable NT synchronization primitives.  
\  - Fix UFS bandwidth votes on the DDR path.  
\  - Default zram to LZ4.  
\  - Disable IPC logging and MMIO access tracing.  
\  - Drop unverified CPU idle and energy model tweaks.  
\  - Reduce charging log spam.  

Learn more at [blog.pixelos.net](https://blog.pixelos.net/)