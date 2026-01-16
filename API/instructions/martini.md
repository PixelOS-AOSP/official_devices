# Prerequisites & Preparation

Before you begin, ensure you have the following:

* **ADB and Fastboot** installed on your computer.
* **USB Debugging** enabled in your phone's Developer Options.
* **Correct Model:** Ensure your device model is exactly **MT2110** or **MT2111**.
* **Stock OS Check:** Boot the device at least once to ensure all functionality works.
* **Remove Google Accounts:** Remove all accounts in Settings to avoid "Factory Reset Protection" (FRP) locks.
* **Back Up Data:** **This process will wipe your phone completely.** Back up everything to your PC or cloud.

# 1. Unlock the Bootloader

1. **Enable OEM Unlock:** Go to **Settings > Developer Options** and enable **OEM unlocking**.
2. **Enter Bootloader Mode:** Connect your phone to the PC. Open a terminal/command prompt and type:

```bash
adb -d reboot bootloader

```
*(Alternatively: Power off, then hold **Volume Up + Volume Down + Power**)*.

3. **Verify Connection:** Type the following to ensure your PC sees the device:
```bash
fastboot devices

```

4. **Unlock:** Type the following command:
```bash
fastboot oem unlock

```

5. **Confirm on Phone:** Follow the on-screen prompts on your phone to confirm the unlock.
6. **Reboot & Re-enable:** If it doesn't reboot automatically, reboot it. You must **re-enable USB debugging** after the device resets.

# 2. Flash Additional Partitions

You need to flash additional files for the recovery to work. Download `dtbo.img`, `vbmeta.img`, and `vendor_boot.img` for your specific device.

1. **Enter Bootloader Mode:** Power off, then hold **Volume Up + Volume Down + Power**.
2. **Flash Files:** Run the following commands one by one (hit Enter after each):
```bash
fastboot flash dtbo dtbo.img
fastboot flash vbmeta vbmeta.img
fastboot flash vendor_boot vendor_boot.img

```

*> **Note:** If you get a "No such file" error, drag and drop the .img file into the terminal window after typing the command to auto-fill the path.*

3. **Reboot to Bootloader:**
```bash
fastboot reboot bootloader

```

# 3. Install PixelOS Recovery

1. **Download Recovery:** Download the `boot.img` provided by the PixelOS team (do not use other recoveries).
2. **Flash Recovery:**
```bash
fastboot flash boot boot.img

```

3. **Enter Recovery:** Use the Volume buttons to navigate the menu on your phone to select **Recovery Mode**, then press Power to select it.

# 4. Install PixelOS

1. **Factory Reset:**
* In the Recovery menu, tap **Factory Reset**.
* Select **Format data / factory reset**.
* Confirm the format.

2. **Prepare for Sideload:**
* Return to the main menu.
* Select **Apply update** > **Apply from ADB**.

3. **Install the ROM:**
* On your computer, type:
```bash
adb -d sideload path/to/PixelOS_file.zip

```

*(Tip: You can type `adb -d sideload ` and then drag the zip file into the terminal).*

> **Note on Success:** The process might stop at **47%** and say `adb: failed to read command: Success` or `Undefined error: 0`. **This is normal and means the installation was successful.**

# 5. Reboot System

1. Once the sideload is complete, return to the main menu.
2. Select **Reboot system now**.

Your device should now boot into PixelOS!
