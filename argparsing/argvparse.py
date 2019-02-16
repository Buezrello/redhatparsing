import argparse


class Argparse:
    """
    A class used for command line parameters parsing

    Attributes
    ----------
        files : list
            list files with text for pattern searching
        regex : str
            regular expression
        underscrore : boolean
            flag, if set - inserting ^^^ under matching text
        color : boolean
            flag, if set - highlight matching text with color
        machine : boolean
            flag, if set - output in machine readable format

    Methods
    -------
        __init__()
            initialization class

        _get_underscore()
            private method, return True if underscore set

        _get_color()
            private method, return True if color set

        _get_machine()
            private method, return True if machine format set

        _get_regex()
            private method, return REGEX

        _get_files()
            private method, return optional files list or None
    """

    def __init__(self):
        """
        Attributes
        ----------
        files : list
            list files with text for pattern searching
        regex : str
            regular expression
        underscrore : boolean
            flag, if set - inserting ^^^ under matching text
        color : boolean
            flag, if set - highlight matching text with color
        machine : boolean
            flag, if set - output in machine readable format
        """

        self.parser = argparse.ArgumentParser()
        # mutual exclusive arguments
        action = self.parser.add_mutually_exclusive_group()
        action.add_argument("-u", "--underscore", action="store_true", dest="underscore",
                            default=False, help="print ^^^ under matching text")
        action.add_argument("-c", "--color", action="store_true", dest="color",
                            default=False, help="highlight matching text")
        action.add_argument("-m", "--machine", action="store_true", dest="machine",
                            default=False, help="machine readable output")
        # required arguments
        required_named = self.parser.add_argument_group("required named arguments")
        required_named.add_argument("-r", "--regex", dest="regex",
                                    help="regular expression, must be enclosed in double or single quotes",
                                    required=True)
        # optional arguments
        self.parser.add_argument("-f", "--files", action="store", dest="files", nargs="*",
                                 help="file(s), if no file provided STDIN required")
        # command line arguments
        self.files = self._get_files()
        self.regex = self._get_regex()
        self.underscore = self._get_underscore()
        self.color = self._get_color()
        self.machine = self._get_machine()

    def _get_underscore(self):
        """
        private method, return True if underscore set

        :return: True or False
        """

        args = self.parser.parse_args()
        return args.underscore

    def _get_color(self):
        """
        private method, return True if color set

        :return: True or False
        """

        args = self.parser.parse_args()
        return args.color

    def _get_machine(self):
        """
        private method, return True if machine format set

        :return: True or False
        """

        args = self.parser.parse_args()
        return args.machine

    def _get_regex(self):
        """
        private method, return REGEX

        :return: REGEX
        """

        args = self.parser.parse_args()
        return args.regex

    def _get_files(self):
        """
        private method, return optional files list
        :return: list of files or None
        """

        args = self.parser.parse_args()
        if args.files:
            return args.files
        else:
            return None
