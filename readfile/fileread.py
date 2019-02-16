import os


class Fileread:
    """
    A class used for file reading

    Attributes
    ----------
        filename : str
            file with absolute or relative path
        shortfilename : str
            file name without path
        lines : list
            list of lines from a file

    Methods
    -------
        __init__(filepath)
            Initialization a class with absolute or relative filename

        read_filelines()
            Inner method that read text from file
    """

    def __init__(self, filepath):
        """
        :param filepath: str
            file with absolute or relative path

        Attributes
        ----------
        filename : str
            file with absolute or relative path
        shortfilename : str
            file name without path
        lines : list
            list of lines from a file
        """

        head, tail = os.path.split(filepath)
        self.filename = filepath
        self.shortfilename = tail
        self.lines = self.read_filelines()

    def read_filelines(self):
        """

        :return: list lines of given file

        Raises
        ------
            Exception on failure file reading
        """

        try:
            with open(self.filename, "r") as infile:
                return infile.readlines()
        except Exception as e:
            # print str(e)
            raise Exception(str(e))
