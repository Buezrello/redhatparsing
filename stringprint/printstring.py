def print_string_simple(string, filename, linenumber):
    print 'File', filename
    print 'String #', linenumber
    print string


def print_string_with_underscore(string, tuples, filename, linenumber):
    line = ''
    for tpl in tuples:
        line = line + (" " * (tpl[0] - len(line))) + ('^' * (tpl[1] - tpl[0]))
    print 'File', filename
    print 'String #', linenumber
    print string
    print line


def print_string_in_color(string, tuples, filename, linenumber):
    line = ''
    endOfPreviousTuple = 0
    for tpl in tuples:
        line = line + string[endOfPreviousTuple: tpl[0]]
        line = line + string[len(line): tpl[0]]
        line = line + '\033[44;33m' + string[tpl[0]:tpl[1]] + '\033[m'
        endOfPreviousTuple = tpl[1]
    line = line + string[endOfPreviousTuple:]
    print 'File', filename
    print 'String #', linenumber
    print line


def print_string_machine_format(string, tuples, filename, linenumber):
    for tpl in tuples:
        print filename + ':' + str(linenumber) + ':' + str(tpl[0]) + ':' + string[tpl[0]: tpl[1]]


