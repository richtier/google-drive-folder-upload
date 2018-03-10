#!/bin/sh
MONITORDIR="$1"
inotifywait -m -r -e create --format '%w%f' "${MONITORDIR}" | while read NEWFILE
do
    python google_drive_folder_upload/main.py "$NEWFILE"
done
