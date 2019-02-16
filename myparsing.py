from stringparsing import pars
from stringprint import printstring
from argparsing import argvparse
from readfile import fileread


class Parsfile:

    def __init__(self):
        self.commandline = ""

    def send_lines_to_finditer(self, pattern, lines, underscore=False, color=False, machine=False, filename=None):
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
        self.commandline = raw_input("Enter string which you want to parse\n")

    def main(self):
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
    # tpl = pars.getStartEndSubstring('[\w\.-]+@[\w\.-]+', 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com')
    # print tpl

    prs = Parsfile()

    # lines = ['guru99@google.com, careerguru88@hotmail.com, hhhhkhkjhkh users@yahoomail.com',
    #          'abff, jjj hkhkhk, yuuu',
    #          'yyyyy, igindin@gmail.com; hkjhkh']
    #
    # prs.send_lines_to_finditer("SomeFileName", '[\w\.-]+@[\w\.-]+', lines)
    # print ''
    # prs.send_lines_to_finditer('Another File', '[\w\.-]+@[\w\.-]+', lines, underscore=True)
    # print ''
    # prs.send_lines_to_finditer('Third File', '[\w\.-]+@[\w\.-]+', lines, color=True)
    # print ''
    # prs.send_lines_to_finditer('MachineFile.txt', '[\w\.-]+@[\w\.-]+', lines, machine=True)

    prs.main()
