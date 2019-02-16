import os


class Fileread:

    def __init__(self, filepath):
        head, tail = os.path.split(filepath)
        self.filename = filepath
        self.shortfilename = tail
        self.lines = self._read_filelines()

    def _read_filelines(self):
        try:
            with open(self.filename, "r") as infile:
                return infile.readlines()
        except Exception as e:
            # print str(e)
            raise Exception(str(e))
