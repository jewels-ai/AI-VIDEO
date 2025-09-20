from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def upload_to_drive(file_path, folder_id=None):
    file_drive = drive.CreateFile({'title': os.path.basename(file_path),
                                   'parents':[{'id': folder_id}] if folder_id else []})
    file_drive.SetContentFile(file_path)
    file_drive.Upload()
    return file_drive['alternateLink']
