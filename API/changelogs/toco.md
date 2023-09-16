# 16-Sep-2023
- Add fastcharge implementation
- Add keylayout mapping for Xbox360 compatible controllers
- Drop unnecessary Google Hotword stuff
- Import Qualcomm CameraX Vendor Extensions
- keylayout: Import joystick keylayouts from 1Controller v1.5.2
- Restore soundtrigger
- sepolicy: Label more wakeup nodes
- wifi: Enable Optimized Power Management

# 20-Aug-2023
- configs: Update dax-default profiles
- Decommonize misys prebuilts
- Disable per-cgroup PSI accounting
- Explicitly disable serial console
- Fix IMS symlink as per dynamic partitions
- parts: Use vector drawable for Dirac™ logo
- prop: Default to boosted color mode
- Switch to Moto Dolby
- Update common blobs from sweet MIUI V14.0.4.0.TKFMIXM

# 13-Jul-2023
- parts: Use vector drawable for Dirac™ logo
- Ship VantomKernel v4.14.320
- Update CarrierConfig from LA.QSSI.13.0.r1-10000.02-qssi.0
- Update system blobs from LA.QSSI.13.0.r1-10000.02-qssi.0

# 09-May-2023
- Ship VantomKernel v4.14.314
- Switch to common Xiaomi 1.0 sensors implementation
- Update blobs from LA.QSSI.13.0.r1-09700-qssi.0
- Update CarrierConfig from LA.QSSI.13.0.r1-09700-qssi.0

# 29-Apr-2023
- Update common blobs from sweet MIUI V14.0.2.0.TKFMIXM

# 20-Apr-2023
- audio: Use 24bit as primary output
- Import Xiaomi TouchFeature service
- overlay: Disable lock screen rotation
- overlay: Disable Pocket Lock
- overlay: Fix hyper orange night light
- overlay: Update battery info every second when charging
- parts: Remove Dirac logo
- parts: Update from sdm845-common
- prop: Redefine bluetooth a2dp offload capabilities
- Restore QCOM wfd HDCP support
- rootdir: Remove deprecated max comp streams
- sepolicy: Address location denials
- sepolicy: Update fast charging perms
- sepolicy: Update some Dolby sepolicy
- Update adreno stack from LA.UM.9.14.r1-21000-LAHAINA.QSSI13.0
- Update ADSP from LA.UM.9.1.r1-12900-SMxxx0.0
- Update blobs from sweet V14.0.1.0.TKFMIXM
- Update gps configs from LA.UM.9.1.r1-12900-SMxxx0.0
- Update keymaster from LA.UM.9.1.r1-12900-SMxxx0.0
- Update some blobs from msmnile LA.UM.9.1.r1-12900-SMxxx0.0
- Update system from LA.QSSI.13.0.r1-09400.01-qssi.0
- Update ueventd from LA.UM.9.1.r1-12900-SMxxx0.0

# 23-Feb-2023
- audio: Fix 24bit audio playback
- dolby: Drop AC4 codec support
- overlay: Disable UI touch sounds by default
- overlay: Use AOSP default ripple animation duration
- powerhint: Set GPU idle timeout to match kernel
- prop: Disable SF composition prediction model
- prop: Force device to treat 170M as sRGB in SF
- rootdir: Delete /data/system/package_cache after updates
- sepolicy: Allow parts to get SettingsLib prop
- sepolicy: Allow system_server to set tethering properties
- Update blobs from sweet V13.0.16.0.SKFMIXM
- Update system from LA.QSSI.13.0.r1-09000.01-qssi.0

# 02-Feb-2023
- configs: Update qdcm display calibration to MIUI V13.0.4.0
- Drop remnant sound_trigger stuff
- Enable AIDL DRM HALs
- gps: Update to LA.UM.9.1.r1-13000-SMxxx0.QSSI13.0
- Inherit several Android Go configurations
- media: Add swap width and height feature
- media: Fix VTS issue
- Move to common Xiaomi displayfeature HIDL
- overlay: Configure SQLite to operate in MEMORY mode
- overlay: Don't pin camera app in memory
- overlay: Restore COLOR_MODE_SATURATED
- overlay: Set google autofill service as default
- overlay: Update pinner configuration from gs201
- parts: Add Dirac logo
- parts: Address services derp
- powerhint: Fix undefined value in Node[PMQoSCpuDmaLatency]
- powerhint: Import camera hints
- powerhint: Restore EnergyAware node
- powerhint: Set camera cpuset to little cores when unused
- prop: Add touch improvements sysprops
- prop: Disable QCRIL power saving
- prop: Disable Skia tracing by default
- prop: Don't set to adaptive mode by default
- prop: Enable apk fs-verity 
- prop: Remove QTI BT stack bits
- prop: RIL edits for battery life
- prop: Switch to AutoSingleLayer A13 setting
- Refactor media configs
- rootdir: Add back UFS sysfs path
- sepolicy: Address denials for audio props
- sepolicy: Address more denials for displayfeature props
- Speed profile services and wifi-service
- Ship Leica camera
- Support udfps on AOD
- Switch to OnePlus Dolby
- Update system blobs from LA.QSSI.13.0.r1-08200-qssi.0

# 30-Nov-2022
- Add permission for Xiaomiparts
- Add xiaomi misys support
- Address various sepolicy denials
- Clean up permissions
- configs: Update public.libraries.txt from stock
- Decommonize battery charger blobs
- overlay: Disable pocket lock support
- dolby: Update dax-default.xml
- Drop remnant sound_trigger stuff
- Drop tetheroffload packages
- Drop vendor.qti.hardware.servicetracker@1.2 HIDL
- Fixup Vulkan deQP permission copy
- Import Xiaomi displayfeature
- Include AndroidAuto at build time
- libinit: Add support of .mod_device hides 
- MiuiCamera with working portrait mode
- overlay: Add default vibration intensites
- parts: Add missing thermal profile permission
- parts: Disable startup provider
- parts: Drop support for Hi-Fi
- parts: Implement Pocket Detection service
- parts: Remove proximity sensor gestures
- parts: Restore MiSound scene on boot complete
- prop: Do not block binder thread on incoming calls
- prop: Don't set to adaptive mode by default
- prop: Enable IncrementalFS support
- prop: For smoother scrolling and better responsiveness
- prop: Pull props for USB controller configuration
- prop: Remove QTI BT stack bits
- rootdir: Enable suspend to RAM
- rootdir: Import oriole cpuctl tuning
- rootdir: Remove package cache on early boot
- Ship VantomKernel v4.14.300
- Switch to common QTI vibrator HAL
- Switch to Pixel thermal HAL
- Switch to sepolicy_vndr-legacy-um
- Update blobs from sweet V13.0.14.0.SKFMIXM
- Update system from LA.QSSI.13.0.r1-07400-qssi.0
- Use LZ4 compression for ramdisks

# 20-Oct-2022
- Initial Android 13 build

# 15-August-2022
- Add more gnss seccomp_policy
- audio: Add compress recording configurations
- audio: Add Stereo config channel support to usb surround sound
- audio: Fix copyright
- audio: Fix in-call mic with headphones
- audio: Fix mic volume
- audio: Import stock audio_policy_engine_stream_volumes.xml
- audio: Increase mic volume values
- audio: Provide missing audio_tuning_mixer.txt
- audio: Remove dynamic attributes from APS config
- audio: Set the maximum music group volume to 15
- audio: Update compress recording configurations
- Build android.hidl.base@1.0
- Build missing omx lib
- Drop remnant Snap stuff
- Drop Vulkan UI renderer (Fixes video colors)
- gps: Add nmea tag block grouping feature
- gps: Comment out ANTENNA_INFO_VECTOR_SIZE by default
- gps: Update configs from sweet V13.0.8.0.SKFMIXM
- gps: Update to LA.UM.9.1.r1-11200-SMxxx0.0
- Import more camera libs from stock
- Make all elf prebuilts packages
- media: Update max resolution from True4k to UHD
- parts: Drop support for zero brightness doze mode
- parts: Update and polish vector drawables
- perfd-client: Refactor dummy libqti-perfd-client 
- perfd-client: Remove namespace declaration
- perfd-client: Return a dummy value
- powerhint: Add F2fsRecessModeEnable
- prop: Fix mic volume in Apps
- prop: Force disable iorapd
- prop: Sync up /system_ext properties with QSSI 12
- Provide module name for libcameraservice
- Re-enable zram writeback
- Rename camera face detection libs
- Restrict interrupts to cores 0 and 1
- rootdir: Add edgnss socket directory
- rootdir: Increase the console log level
- rootdir: Set Netflix property based on target
- rootdir: Set permissions for KGSL sysfs node
- rootdir: Stop using hardcoded boot device
- sepolicy: Add F2FS sysfs permission
- sepolicy: Address camera hal denial
- sepolicy: Address dpmd denial
- sepolicy: Address dolby denials
- sepolicy: Address mi_thermald-related denials
- sepolicy: Address neuralnetworks hal neverallow
- sepolicy: Address some duplicate
- sepolicy: Address some wifi denials
- sepolicy: Allow bluetooth to read incremental prop
- sepolicy: Allow radio to connect to dpmd stream socket
- sepolicy: Extend vendor_toolbox permissions to files in persist
- sepolicy: Fix setting ims props on boot
- sepolicy: Label new telephony properties
- sepolicy: Rework & label more wakeup nodes
- sepolicy: Suppress zeroth.debuglog.logmask warning
- Set soc properties
- Ship VantomKernel v4.14.290
- udfps: Refactor udfps handler lib
- Update adreno stack from from LA.UM.9.14.r1-19300.01-LAHAINA.QSSI12.0
- Update blobs from sweet V13.0.8.0.SKFMIXM
- Update blobs from sweet V13.0.12.0.SKFMIXM
- wifi: Update from sweet V13.0.8.0.SKFMIXM
- WifiSM6150: Add & increase 5 GHz network signal tolerance
- WifiSM6150: Align config.xml with AOSP

# 08-July-2022
- Add telephony system-ext privapp permissions
- Address elliptic denials
- Allow platform app to find SoterService
- Allow system_app to write thermal sysfs
- Display icon beside thermal profiles
- Drop QCOM wfd HDCP support
- Fix fingerprint labels
- Import lmkd props from google gki
- Label fingerprint props as restricted vendor
- Move deviceid props to vendor
- parts: Don't explicitly set android:theme for activities
- Remove unused hwservice label
- Rename ANXCamera to MiuiCamera
- Revoke system_server access to fingerprint prop
- Ship VantomKernel v4.14.286

# 23-June-2022
- Add missing status bar dimensions
- Fix ANXCamera after updating blobs
- Fix data decryption in TWRP

# 21-June-2022
- Address QCOM WFD denials
- Disable zram writeback
- Don't enable iostats
- Don't tune sde partition on boot
- Drop firmware inclusion (Install firmware separately)
- Drop QCOM thermal engine components
- Drop updatable GPU drivers
- Enable auto brightness while dozing
- Fix UDFPS not registering
- Implement UDFPS handler
- Import dolby codecs
- June security patch level
- media: Finetune performance xml
- Move to common Xiaomi fingerprint HIDL
- Override odm_dlkm and vendor_dlkm props
- parts: Add dynamic thermal profile implementation
- parts: Handle more errors for dirac
- parts: Use directBootAware
- Pull sepolicy from SM8250
- Ship VantomKernel v4.14.282
- Support F2FS compression and garbage collector
- Switch SchedTune to UClamp
- Switch to EROFS for dynamic partitions
- Switch to status_bar_height_portrait
- Sync brightness overlays with coral
- Update blobs from LA.QSSI.12.0.r1-07100-qssi.0
- Update build fp & desc to MIUI V13.0.2.0.SFNMIXM
- Update display color compositions
- Update system WFD blobs from 07100
- Uprev radio config into 1.2
- Use coral tuning for columbus feature

# 07-May-2022
- May security patch level
- Introducing built-in ANXCamera
- Add 300Mhz minimum CPU scaling frequency
- Build IFAAService from source
- Import more camera blobs
- Increase volume steps from 15 to 25
- Update safe media volume index
- Power HAL improvements
- Switch to common Xiaomi light AIDL
- Address more denials
- VantomKernel v4.14.276 improvements
- Disable wallpaper zooming
- Switch to PlayGround clang
- Wi-Fi HAL improvements
- Switch to a custom QTI vibrator AIDL

# 02-May-2022
- Initial official and stable build based on Android 12.1
