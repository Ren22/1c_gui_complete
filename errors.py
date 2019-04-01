import os


class spaceMError(Exception):
    def __init__(self, msg=None):
        self.message = msg


def check_paths(*paths):
    for path in paths:
        try:
            os.path.getsize(path)
        except OSError as err:
            if not path:
                raise spaceMError('One of the paths to the file was not provided')
            else:
                raise spaceMError(err)