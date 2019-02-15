from stringparsing import pars
from stringprint import printstring


class Parsfile:

    def send_lines_to_finditer(self, filename, pattern, lines, underscore=False, color=False, machine=False):
        count = 0
        for ln in lines:
            count += 1
            tuples = pars.getStartEndSubstring(pattern, ln)
            if tuples:
                if underscore:
                    printstring.print_string_with_underscore(ln, tuples, filename, count)
                elif color:
                    printstring.print_string_in_color(ln, tuples, filename, count)
                elif machine:
                    printstring.print_string_machine_format(ln, tuples, filename, count)
                else:
                    printstring.print_string_simple(ln, filename, count)


if __name__ == '__main__':
    # tpl = pars.getStartEndSubstring('[\w\.-]+@[\w\.-]+', 'guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com')
    # print tpl

    lines = ['guru99@google.com, careerguru88@hotmail.com, hhhhkhkjhkh users@yahoomail.com',
             'abff, jjj hkhkhk, yuuu',
             'yyyyy, igindin@gmail.com; hkjhkh']

    prs = Parsfile()
    prs.send_lines_to_finditer("SomeFileName", '[\w\.-]+@[\w\.-]+', lines)
    print ''
    prs.send_lines_to_finditer('Another File', '[\w\.-]+@[\w\.-]+', lines, underscore=True)
    print ''
    prs.send_lines_to_finditer('Third File', '[\w\.-]+@[\w\.-]+', lines, color=True)
    print ''
    prs.send_lines_to_finditer('MachineFile.txt', '[\w\.-]+@[\w\.-]+', lines, machine=True)
