import base64
import os
import pathlib

import dropbox
from dropbox.exceptions import HttpError

my_token = base64.b64decode(
    'c2wuQkVfdmpiTUJNNGRUUVBYREJPM20xb2lDZVkxbC1PSlpNd0R6T3FqdE15WUxOOTQzUWt0SFFaYU1hUEZK'
    'N0UzSWR0T21ScjFRM3lWZmtEUWs3YXJtUW1nblk0Q3dqdHU0SkdLUjdudU5ma3h2c2NlZFdaNFFsSXJIalc2YjNOQTJwY1JqbVZLN2txRlM=')\
    .decode('utf-8')


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
