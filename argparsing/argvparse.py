import argparse


class Argparse:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        # mutual exclusive arguments
        action = self.parser.add_mutually_exclusive_group()
        action.add_argument("-u", "--underscore", action="store_true", dest="underscore",
                            default=False, help="Print ^^^ under matching text")
        action.add_argument("-c", "--color", action="store_true", dest="color",
                            default=False, help="Highlight matching text")
        action.add_argument("-m", "--machine", action="store_true", dest="machine",
                            default=False, help="Machine readable output")
        # required arguments
        required_named = self.parser.add_argument_group("required named arguments")
        required_named.add_argument("-r", "--regex", dest="regex", help="Regular expression", required=True)
        # optional arguments
        self.parser.add_argument("-f", "--files", action="store", dest="files",
                                 help="File(s). If no file provided STDIN required")
        # command line arguments
        self.files = self._get_files()
        self.regex = self._get_regex()
        self.underscore = self._get_underscore()
        self.color = self._get_color()
        self.machine = self._get_machine()

    def _get_underscore(self):
        args = self.parser.parse_args()
        return args.underscore

    def _get_color(self):
        args = self.parser.parse_args()
        return args.color

    def _get_machine(self):
        args = self.parser.parse_args()
        return args.machine

    def _get_regex(self):
        args = self.parser.parse_args()
        return args.regex

    def _get_files(self):
        args = self.parser.parse_args()
        if args.files:
            return args.files
        else:
            return None
