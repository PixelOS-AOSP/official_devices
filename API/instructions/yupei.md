# Before installing notes
- Please follow the installation guide properly to avoid running into troubles.
- Make sure your stock firmware build number is equal to or higher than `OS3.0.303.0`.
- All models are supported, as long as they are unlockable.
- Remove all Google accounts before proceeding to avoid FRP (Factory Reset Protection) locks.
- Also, remember to back up your data. We are not responsible for data loss.

# Unlocking the bootloader
- First of all, enable OEM unlock, as well as USB debugging in Developer Options.
- Go to `Mi Unlock status` in Developer Options and add your Xiaomi account - you can only continue once the waiting period Xiaomi gives you is over.
- Then on the computer, open Command Prompt (Windows) or a terminal (Linux/macOS), then type:
```
adb -d reboot bootloader
```
- Once the device is in fastboot mode, verify your PC finds it by typing:
```
fastboot devices
```
> TIP: If you see `no permissions fastboot` while on Linux or macOS, try running fastboot as root.
- Follow the instructions on [Xiaomi’s official unlocking website](https://en.miui.com/unlock/) to unlock the bootloader of your device with the Mi Unlock tool.
- Wait for the tablet to reboot. You might want to let the device fully boot into the system before proceeding further.

# Flashing PixelOS recovery
- In order to flash recovery, go to Fastboot mode by shutting down the tablet, then hold the Volume Down and Power buttons.
- Then, flash recovery using these commands (run them one by one):
```
fastboot flash boot boot.img
fastboot flash dtbo dtbo.img
fastboot flash init_boot init_boot.img
fastboot flash recovery recovery.img
fastboot flash vendor_boot vendor_boot.img
```

> **Note:** If you get a "No such file" error, drag and drop the .img file into the terminal window after typing the command to auto-fill the path.

- After that, reboot to recovery by using this command:
```
fastboot reboot recovery
```

> If your recovery does **not** show the PixelOS logo, you accidentally booted into the wrong recovery. Please start at the top of this section!

# Make sure the same firmware is flashed in both slots
You can safely ignore this section if your firmware is flashed in both slots. If you are unsure, or you don't have them installed in both slots before installing, follow the instruction below.

In some cases, the inactive slot can be unpopulated or contain much older firmware than the active slot, leading to various issues including a potential hard-brick. We can ensure none of that will happen by copying the contents of the active slot to the inactive slot.

To do this, download the [copy-partitions-20220613-signed.zip](https://mirrorbits.lineageos.org/tools/copy-partitions-20220613-signed.zip) package by doing the following:
- From PixelOS recovery, select `Apply update`, then `Apply from ADB` to begin sideload.
- On the host machine, sideload the package using this command:
```
adb -d sideload copy-partitions-20220613-signed.zip
```
> Note: The copy-partitions script was created by LineageOS developer erfanoabdi and filipepferraz
- Now reboot to recovery by tapping `Advanced`, then `Reboot to recovery`.

# Flashing PixelOS
- First of all, go to `Factory Reset` and select `Format data/factory reset` then confirm the format. This needs to be done before installing the ROM.
- Download the PixelOS ROM file using the **Download** button above.
- Flash the ROM:
    - On the device, select `Apply update`, then `Apply from ADB` to begin sideload.
    - On the host machine, sideload the package using:
    ```
    adb -d sideload /path/to/zip
    ```
    > If signature verification fails, that means the ROM you are trying to flash is either corrupted, or not an official PixelOS ROM. Please redownload the ROM.
    > Normally, adb reports `Total xfer: 1.00x`, but in some cases, even if the process succeeds, the output may stop at 47% and show `adb: failed to read command: Success`. In other instances, it might display `adb: failed to read command: No error` or `adb: failed to read command: Undefined error: 0` which is also fine.
- Once flashing is complete, hit `Reboot system now`.
> Note: The first boot usually takes no longer than 15 minutes, depending on the device. If it takes longer, you may have missed a step, otherwise feel free to get assistance in the PixelOS Telegram chat.
- Have fun with your shiny new PixelOS installation!