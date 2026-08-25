# General Instructions

* Make sure the device has an unlocked bootloader before proceeding.
* Make sure the device is running the latest **NothingOS 3.2 firmware**.
* Clean flash when coming from a different Custom ROM or Stock.
* Make sure you have the required ADB/Fastboot drivers and [platform tools](https://developer.android.com/tools/releases/platform-tools) installed. It is advised to add platform tools to the PATH environment variable.
* Do NOT attempt to change the recovery or kernel from what is included with PixelOS.

# Clean Flash

Clean flash involves formatting data, which means you will be losing all data stored in the internal storage of your device. Keep a backup of anything important before proceeding.

1. Download the following files:

   * `boot.img`
   * `vendor_boot.img`
   * `PixelOS_Spacewar.zip`

2. Boot the device into bootloader mode by either:

   * running the command `adb reboot bootloader` (if USB Debugging is enabled), or
   * with the device powered off, holding the appropriate key combination to enter the bootloader.

3. Flash the downloaded image files to your device by running:

```bash
fastboot flash boot path/to/boot.img
fastboot flash vendor_boot path/to/vendor_boot.img
```

4. Reboot to recovery by either:

   * using the volume buttons to navigate and selecting the `Recovery Mode` option, or
   * running:

```bash
fastboot reboot recovery
```

```
You should be greeted with PixelOS Recovery.
```

5. Tap `Factory Reset`, then `Format data / factory reset` and confirm the operation. **THIS WILL WIPE YOUR DATA.**

6. Return to the main menu and select `Apply update`, then `Apply from ADB` to begin sideload.

7. Sideload the `PixelOS_Spacewar.zip` file by running:

```bash
adb -d sideload /path/to/PixelOS_Spacewar.zip
```

```
Normally, adb reports `Total xfer: 1.00x`, but in some cases, even if the installation succeeds, the output may stop at 47% or display messages such as `adb: failed to read command: Success`, `adb: failed to read command: No error`, or `adb: failed to read command: Undefined error: 0`. This is normal as long as the recovery reports that the installation completed successfully.
```

8. Go back to the main menu and select `Reboot system now`.

```
The first boot may take several minutes. If the device does not boot after an unusually long time, verify that all the steps above were followed correctly.
```

# Dirty Flash / Update

There should be no loss of data when updating from an existing PixelOS installation. However, keeping a backup is recommended in case anything goes wrong.

1. Download the following file:

   * `PixelOS_Spacewar.zip`

2. Reboot to recovery by either:

   * booting into the bootloader and selecting the `Recovery Mode` option using the volume and power buttons, or
   * running:

```bash
adb reboot recovery
```

```
You should be greeted with PixelOS Recovery.
```

3. From the main menu, select `Apply update`, then `Apply from ADB` to begin sideload.

4. Sideload the `PixelOS_Spacewar.zip` file by running:

```bash
adb -d sideload /path/to/PixelOS_Spacewar.zip
```

```
Normally, adb reports `Total xfer: 1.00x`, but in some cases, even if the installation succeeds, the output may stop at 47% or display messages such as `adb: failed to read command: Success`, `adb: failed to read command: No error`, or `adb: failed to read command: Undefined error: 0`. This is normal as long as the recovery reports that the installation completed successfully.
```

5. Go back to the main menu and select `Reboot system now`.

```
The first boot after an update may take several minutes.
```
