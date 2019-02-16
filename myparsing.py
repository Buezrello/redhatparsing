from stringparsing import pars
from stringprint import printstring
from argparsing import argvparse
from readfile import fileread


class Parsfile:
    """
    Main class for reading user input

    Attributes
    ----------
        commandline : str
            optional command line - contains STDIN input when files were not specified

    Methods
    -------
        __init__()
            class initialization

        send_lines_to_finditer(pattern, lines, underscore, color, machine, filename=None)
            read file list or input string, send lines for pattern searching

        read_user_input()
            read user input - if no files were given

        main()
            main method, called for starting job

    """

    def __init__(self):
        """
        Initialization class
        """

        self.commandline = ""

    def send_lines_to_finditer(self, pattern, lines, underscore=False, color=False, machine=False, filename=None):
        """
        Attributes
        ----------
        pattern : str
            REGEX
        lines : list
            list of strings for pattern matching
        underscrore : boolean
            flag, if set - inserting ^^^ under matching text
        color : boolean
            flag, if set - highlight matching text with color
        machine : boolean
            flag, if set - output in machine readable format
        filename : list
            list of files

        :param pattern: REGEX
        :param lines: list of lines in file or line from STDIN
        :param underscore: if set underscore matching with ^^^
        :param color: if set highlight matching with color
        :param machine: if set print outout in machine readable format
        :param filename: file with text for pattern matching
        """

        if filename:
            prnt = printstring.Printstring(filename=filename)
        else:
            prnt = printstring.Printstring()
        prs = pars.Parsstring()
        count = 0
        for ln in lines:
            count += 1
            tuples = prs.getStartEndSubstring(pattern, ln)
            if tuples:
                if underscore:
                    prnt.print_string_with_underscore(ln, tuples, count)
                elif color:
                    prnt.print_string_in_color(ln, tuples, count)
                elif machine:
                    prnt.print_string_machine_format(ln, tuples, count)
                else:
                    prnt.print_string_simple(ln, count)

    def read_user_input(self):
        """
        Read user STDIN input, if no files were given
        """

        self.commandline = raw_input("Enter string which you want to parse\n")

    def main(self):
        """
        main method, called for starting job
        """

        argprs = argvparse.Argparse()

        lines = []

        if not argprs.files:
            self.read_user_input()
            lines.append(self.commandline)
            self.send_lines_to_finditer(argprs.regex, lines,
                                        argprs.underscore, argprs.color, argprs.machine)
        else:
            # print argprs.files
            for fl in argprs.files:
                try:
                    filerd = fileread.Fileread(fl)
                    self.send_lines_to_finditer(argprs.regex, filerd.lines,
                                                argprs.underscore, argprs.color, argprs.machine,
                                                filerd.shortfilename)
                except Exception as e:
                    print str(e), "\n"


if __name__ == '__main__':

    prs = Parsfile()
    prs.main()
