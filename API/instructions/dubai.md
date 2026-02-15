# General Instructions

- Make sure the model of the device is exactly `XT2203-1`
- Make sure the device has an unlocked bootload. If not, follow steps [here](https://en-us.support.motorola.com/app/standalone/bootloader/unlock-your-device-a)
- Clean flash when coming from a different Custom ROM or Stock
- Make sure to have installed all the required drivers from [here](https://en-us.support.motorola.com/app/usb-drivers) and platform tools from [here](https://developer.android.com/tools/releases/platform-tools). It is advised to add platform tools to the PATH environment variable, follow instructions [here](https://github.com/alexal1/Insomniac/wiki/Adding-platform-tools-to-the-PATH-environment-variable)
- Do NOT attempt to change recovery or kernel from what is included.


# Clean Flash
Clean flash involves formatting data which means you will be loosing data stored in the internal storage of your device. I will not be responsible for any loss of data.
1. Download the following files:
    - `dtbo.img`
    - `vendor_boot.img`
    - `boot.img`
    - `PixelOS_dubai.zip`
2. Boot the device into bootloader mode by either:
    - running the command `adb reboot bootloader` (if USB Debugging is enabled) or
    - with the device powered off, hold `Volume Down` + `Power` buttons.
3. Flash the downloaded image files to your device by typing:
```
fastboot flash dtbo path/to/dtbo.img
fastboot flash vendor_boot path/to/vendor_boot.img
fastboot flash boot path/to/boot.img
```
4. Reboot to recovery by either:
    - using the volume buttons to navigate, select the `Recovery Mode` option or
    - by running the command `fastboot reboot recovery`
    
    You Should be greeted with PixelOS Recovery
5. In some cases, the inactive slot can be unpopulated or contain much older firmware than the active slot. To be safe:
    - Download the copy-partitions-20220613-signed.zip file from [here](https://mirrorbits.lineageos.org/tools/copy-partitions-20220613-signed.zip)
    - On the device, select `Apply update`, then `Apply from ADB` to begin sideload
    - Sideload the package using the command `adb -d sideload copy-partitions-20220613-signed.zip`
    
    Thanks to erfanoabdi and filipepferraz for creating this script.
6. Now reboot to recovery by tapping `Advanced`, then `Reboot to recovery`.
7. Now tap Factory Reset, then Format data / factory reset (THIS WILL WIPE YOUR DATA)
8. Return to the main menu and select `Apply update`, then `Apply from ADB` to begin sideload.
9. Sideload the `PixelOS_dubai.zip` file by running the command `adb -d sideload /path/to/zip`. After the package is installed, recovery will inform you that reboot to recovery is required to install add-ons. Select “No”.


    Normally, adb reports Total xfer: 1.00x, but in some cases, even if the process succeeds, the output may stop at 47% and show adb: failed to read command: Success. In other instances, it might display adb: failed to read command: No error or adb: failed to read command: Undefined error: 0 which is also fine

10. Go the main menu, select `Reboot system now` and voila!

    The first boot usually takes no longer than 15 minutes, depending on the device. If it takes longer, you may have missed a step, otherwise feel free to get assistance.

# Dirty Flash / Update

There will be no loss of data if everything goes well. Keep backups incase of any mishap. I will not be responsible for any loss of data.

1. Download the following file:
    - `PixelOS_dubai.zip`
2. Reboot to recovery by either:
    - with the device powered off, hold `Volume Down` + `Power` buttons, using the volume buttons to navigate, select the `Recovery Mode` option or
    - by running the command `adb reboot recovery`
    
    You Should be greeted with PixelOS Recovery
3. From the main menu and select `Apply update`, then `Apply from ADB` to begin sideload.
4. Sideload the `PixelOS_dubai.zip` file by running the command `adb -d sideload /path/to/zip`. After the package is installed, recovery will inform you that reboot to recovery is required to install add-ons. Select “No”.


    Normally, adb reports Total xfer: 1.00x, but in some cases, even if the process succeeds, the output may stop at 47% and show adb: failed to read command: Success. In other instances, it might display adb: failed to read command: No error or adb: failed to read command: Undefined error: 0 which is also fine

5. Go the main menu, select `Reboot system now` and voila!

    The first boot usually takes no longer than 15 minutes, depending on the device. If it takes longer, you may have missed a step, otherwise feel free to get assistance.

