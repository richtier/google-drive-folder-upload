import argparse
import os

import client, helpers


def main():
    parser = argparse.ArgumentParser('Upload images to Google Drive')
    parser.add_argument('file_path', type=str, help='Path of file to upload')
    parser.add_argument(
        '--humans_only', dest='humans_only', help='Upload only human pictures'
    )

    options = parser.parse_args()

    google_drive_client = client.GoogleDriveClient()
    google_vision_client = client.GoogleVisionClient()

    if options.humans_only:
        should_upload = google_vision_client.is_human(path=options.file_path)
    else:
        should_upload = True

    if should_upload:
        google_drive_client.upload_file(path=options.file_path)
    os.remove(options.file_path)


if __name__ == '__main__':
    main()
