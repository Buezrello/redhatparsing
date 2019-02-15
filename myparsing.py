from stringparsing import pars
from stringprint import printstring
from argparsing import argvparse


class Parsfile:

    def send_lines_to_finditer(self, filename, pattern, lines, underscore=False, color=False, machine=False):
        prnt = printstring.Printstring(filename=filename)
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

    def main(self):
        argprs = argvparse.Argparse()
        #temporary - testing argument parsing
        print 'files =', argprs.files
        print 'regex =', argprs.regex
        print 'underscore =', argprs.underscore
        print 'color =', argprs.color
        print 'machine =', argprs.machine


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
