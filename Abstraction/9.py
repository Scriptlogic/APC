from abc import ABC, abstractmethod

class CloudStorage(ABC):

    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")


class OneDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to OneDrive")

    def download_file(self):
        print("File downloaded from OneDrive")

    def delete_file(self):
        print("File deleted from OneDrive")


class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox")

    def download_file(self):
        print("File downloaded from Dropbox")

    def delete_file(self):
        print("File deleted from Dropbox")


g = GoogleDrive()
g.upload_file()
g.download_file()
g.delete_file()

o = OneDrive()
o.upload_file()
o.download_file()
o.delete_file()

d = Dropbox()
d.upload_file()
d.download_file()
d.delete_file()