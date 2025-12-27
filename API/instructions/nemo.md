### Pre-installation
* Download the latest ROM file.
* Download support files from the site:
  - **recovery.img**
* Ensure you are on realmeUI 2.0 firmware.
* Make sure your bootloader is already unlocked.

---

### Step 1: Flash Recovery 
**This step can be skipped if you have compatible custom recovery.**

1. Download and keep support files ready.

2. On the computer, open a command prompt (on Windows) or terminal (on Linux or macOS) window, and type:

```
adb reboot bootloader
```

3. Once the device is in fastboot mode, verify your PC finds it by typing:

```
fastboot devices
```

4. Flash the downloaded image files to your device by typing:

```
fastboot flash recovery recovery.img
```

5. Now reboot into recovery to verify the installation. Do **not** reboot into the existing OS, since it will overwrite the recovery you just installed!

*Note: If your recovery does not show the PixelOS logo, you accidentally booted into the wrong recovery. Please start at the top of this section!*

### Step 2: Flash ROM
**This step can be also used for update installation**

1. Ensure you have downloaded latest PixelOS package from the link above

2. If you are not in recovery, reboot into recovery.

3. For clean / first-time installation - Tap **Factory Reset** > **Format data** and continue with the formatting process. This will remove encryption and delete all files stored in the internal storage, as well as format your cache partition (if you have one). This step can be skipped for update installation.

4. Return to the main menu.

5. Sideload the PixelOS package but do not reboot before you read/followed the rest of the instructions!
  - On the device, tap **Apply Update** > **Apply from ADB** to begin sideload.
  - On the host machine, sideload the package using:

```
adb sideload pixelos.zip
```
---