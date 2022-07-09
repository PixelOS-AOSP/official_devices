git config --global user.name "PixelOS-Bot"
git config --global user.email "pixelos.pixelish@gmail.com"
git fetch
git pull
git add .
git commit -m "official_devices: update tags [no ci]"
git push origin twelve
