import argparse
import os

import client


def main():
    parser = argparse.ArgumentParser('Upload images to Google Drive')
    parser.add_argument('file_path', type=str, help='Path of file to upload')
    options = parser.parse_args()

    google_drive_client = client.GoogleDriveClient()

    google_drive_client.upload_file(path=options.file_path)
    os.remove(path)


if __name__ == '__main__':
    main()
