import os

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


class GoogleDriveClient:


    def __init__(self):
        authenticator = GoogleAuth()
        authenticator.LocalWebserverAuth()
        self.drive = GoogleDrive(authenticator)

    def upload_file(self, path):
        dirname = os.path.dirname(path)
        folder = self.get_or_create_folder(dirname)
        file_name = os.path.basename(path)
        file = self.drive.CreateFile({
            'title': file_name,
            'parents': [{'kind': 'drive#fileLink', 'id': folder['id']}]
        })
        file.SetContentFile(path)
        file.Upload()

    def get_or_create_folder(self, title):
        files = self.drive.ListFile({
            'q': 'title = "{title}" and trashed=false'.format(title=title),
            'maxResults': 1
        }).GetList()
        if files:
            folder = files[0]
        else:
            folder = self.drive.CreateFile({
                'title' : title,
                'mimeType' : 'application/vnd.google-apps.folder'
            })
            folder.Upload()
        return folder
