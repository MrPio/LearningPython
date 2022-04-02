import os
import pathlib

import dropbox
from dropbox.exceptions import HttpError

my_token = "sl.BE_CUFUywNKFPu8ta6RDq2wDtfFSDWBa5XxmZHjKPl6ZHXqW2dOnn7SsE66wxYIGfNShYZLcQWdg7JHYUqytoDuOW1J38mm5pguDYN32SgZB-PtItSghAh_Lznf8XaT0r2See7UiF3K4"


class DropboxAPI:
    def __init__(self, token, folder="/", name=None):
        super().__init__()
        self.dbx = dropbox.Dropbox(token)
        self.folder = folder
        self.name = name

    def download(self):
        """Download a file.
        Return the bytes of the file, or None if it doesn't exist.
        """
        path = '%s%s' % (self.folder.replace(os.path.sep, '/'), self.name)
        while '//' in path:
            path = path.replace('//', '/')
        try:
            md, res = self.dbx.files_download(path)
        except HttpError as err:
            print('*** HTTP error', err)
            return None
        data = res.content
        print(len(data), 'bytes; md:', md)
        return data


db = DropboxAPI(my_token, name='Pink Floyd.flac')
desktop_path = pathlib.Path.home() / 'Desktop'
open(desktop_path.__str__() + "/Pink Floyd - One Of My Turns.flac", "wb").write(db.download())
