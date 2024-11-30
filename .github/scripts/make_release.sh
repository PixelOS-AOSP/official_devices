#!/bin/bash

function download_release() {
    cd releases

    gh release download $tag

    # Merge files conditionally
    if [[ -f checksum.txt ]]; then
        echo "Split files detected, merging ..."
        filename=$(basename PixelOS*zipaa | sed 's/.zipaa/.zip/')
        cat PixelOS*.zip* >>$filename
        rm -r PixelOS*.zipa*

        # Verify checksum
        md5=$(md5sum $filename | awk '{print $1}')
        checksum=$(cat checksum.txt | awk '{print $1}')

        if [[ $checksum = $md5 ]]; then
            echo "Checksum verified!"
        else
            echo "Checksum verification failed!"
            exit 1
        fi
    fi

    cd -
}

function upload_release() {
    cd releases

    filename=$(basename PixelOS*.zip)

    # Upload ROM
    sshpass -p $ssh_pass scp -o "StrictHostKeyChecking no" $filename \
        "pixelos@frs.sourceforge.net:/home/frs/project/pixelos-releases/$version_string/$codename/$filename"

    # Upload recovery images
    if [ "$(ls *.img 2>/dev/null | wc -l)" -gt 1 ]; then
        # Create a folder for multiple images
        folder_name=$(echo $filename | grep -oE '[0-9]{8}-[0-9]{4}')
        mkdir $folder_name
        mv *img $folder_name
        sshpass -p $ssh_pass scp -r -o "StrictHostKeyChecking no" $folder_name \
            "pixelos@frs.sourceforge.net:/home/frs/project/pixelos-releases/$version_string/$codename/recovery/$folder_name"
    else
        recovery_file=$(basename *.img)
        sshpass -p $ssh_pass scp -o "StrictHostKeyChecking no" $recovery_file \
            "pixelos@frs.sourceforge.net:/home/frs/project/pixelos-releases/$version_string/$codename/recovery/$recovery_file"
    fi

    cd -
}
