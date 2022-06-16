## Flashing Instructions

### Clean flash - Encrypted (coming from a different ROM):
- Download ROM from the link above
- Download Magisk (optionally)
- Reboot to recommended recovery
- Format data (if encrypted)
- Wipe system, vendor, cache, dalvik, data, system_ext
- Flash latest firmware (link above)
- Flash ROM zip
- Reboot
- To get root access, reboot to recovery after ROM setup and flash magisk.

### Clean flash - Decrypted:
- Download ROM from the link above
- Download Magisk (optionally)
- Download DFE
- Reboot to recommended recovery
- Wipe system, vendor, cache, dalvik, data, system_ext
- Flash latest firmware (link above)
- Flash ROM zip
- Flash DFE
- Reboot
- To get root access, reboot to recovery after ROM setup and flash magisk.

### Updating to a newer build (dirty flash):
- Wipe cache, dalvik and system_ext
- Flash ROM zip, DFE (if decrypted) and magisk (optional) and reboot