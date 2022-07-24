# PixelOS Official Devices API
## Purpose
This folder contains information of official Devices in ```<codename>.json``` format. This will be helpful for things 
like Automatic Updates Poster and our [website](https://pixelos.vercel.app/). New maintainers are required to create a pull request to this repository to add their 
devices. 
## Format 
```json
{
    "maintainer":[
        {
            "display_name": "Maintainer1",
            "telegram": "https://t.me/Maintainer1",
            "github": "https://github.com/Maintainer1"
        },
        {
            "display_name": "Maintainer2",
            "telegram": "https://t.me/Maintainer2",
            "github": "https://github.com/Maintainer2"
        }
    ],
    "updater": true,
    "beta": false,
    "version": "twelve",
    "release": "monthly",
    "device_display_name": "Redmi Note 8 PUBG Edition",
    "device_display_codename": "ginkgo/willow",
    "public_download": "https://www.download.com",
    "last_updated": "6 September 2022",
    "private_download_tag": "ginkgo_20220105_2327",
    "active": true,
    "xda": null,
    "customRecoveryRequired": true
}
```
## Variables

### Maintainer Information

```display_name```: What the maintainer would like be to be referred as

```telegram```: Link to maintainers Telegram Profile

```github```: Link to Github profile of the maintainer

The above 3 can be different for each maintainer. 

```active```: If the maintainer is currently active in maintaining this device 

```xda```: XDA Thread maintained by the device maintainer for his builds.

### Build Information

```updater```: When set to true, pushes an OTA Update and creates a post for Telegram Channel. When set to false, only 
creates a post for Telegram Channel. Should be set to true only if the build is fit to be dirty flashed over the previous 
official build

```beta```: Should be set to true if the build is in a beta stage and would take time to get stable

```version```: Corresponding branch name of the manifest used to sync PixelOS

```release```: Release type ie. Monthly, Weekly, Daily, etc.

```public_download```: Download link which is to be shared Through Telegram; **New maintainers must set this to ```""```
(two double quotes with nothing between them) until the first update**

```last_updated```: Date of the latest update. Should be in the format ```dd MMMM YYYY``` as per [unicode](http://unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns). Example has been provided in the code snippet [above](https://github.com/PixelOS-Pixelish/official_devices/tree/twelve/API/devices#format)

```private_download_tag```: Github releases tag, to be taken from CI Builds; **New maintainers must set this to ```""```
(two double quotes with nothing between them) until the first update**

```customRecoveryRequired```: Is the recovery built with the ROM also the reccomended recovery to flash PixelOS

### Device Information

```device_display_name```: Name of the Device given by the Brand

```device_display_codename```: codename of the device, if there are multiple codename, split it with a ```/```



