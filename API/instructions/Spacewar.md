## Prerequisites
*   **Unlocked Bootloader:** Your device must already have an unlocked bootloader.
*   **Firmware Requirement:** Ensure you are on the latest NothingOS 3.2 firmware before proceeding.
*   **Platform Tools:** ADB and Fastboot must be installed on your PC.
*   **Required Files:** Download the latest release files to your PC and place them in the same folder as your platform tools (or open your terminal directly in that folder):
    *   `PixelOS_Spacewar-XX.X-XXXXXXXX-XXXX.zip`
    *   `boot.img`
    *   `vendor_boot.img`

---

## Installation Steps

### Step 1: Boot into Fastboot Mode
Connect your phone to your PC. Open your terminal/command prompt in the directory where your downloaded files are located and run:
```bash
adb devices
adb reboot bootloader
```

### Step 2: Verify Fastboot Connection
Ensure your PC recognizes the device in bootloader mode:
```bash
fastboot devices
```
*If you don't see your device serial number, ensure you have the correct fastboot USB drivers installed.*

### Step 3: Flash the Boot Image
Flash the boot partition to install the custom recovery environment:
```bash
fastboot flash boot boot.img
```

### Step 4: Flash the Vendor Boot Image
Next, flash the vendor boot partition:
```bash
fastboot flash vendor_boot vendor_boot.img
```

### Step 5: Reboot to Recovery
Use your phone's physical volume buttons to cycle through the bootloader menu until it displays **Recovery Mode**. Press the Power button to select it. Your phone will now boot into the PixelOS Recovery.

### Step 6: Factory Reset (Wipe Data)
To prevent bootloops and conflicts with old system data, you must format the device:
1. In the recovery menu, tap **Factory Reset**.
2. Tap **Format data / factory reset**.
3. Confirm the action and wait for it to complete.

### Step 7: Sideload the ROM
Now it's time to install PixelOS:
1. Go back to the main recovery menu.
2. Tap **Apply update**.
3. Tap **Apply update from ADB**.
4. In your PC terminal, execute the sideload command:
```bash
adb sideload PixelOS_Spacewar-XX.X-XXXXXXXX-XXXX.zip
```
*(Note: It is completely normal for the terminal to stop at 47% or report "Step 2/2". Please be patient and wait for the phone's screen to confirm that the installation is complete).*

### Step 8: Reboot to System
Once the installation finishes, tap the back arrow in the top left of the recovery screen and select **Reboot system now**.

🎉 **Enjoy PixelOS!**
