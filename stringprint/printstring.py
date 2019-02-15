class Printstring:

    def __init__(self, filename='<commandline>'):
        self.filename = filename

    def print_string_simple(self, string, linenumber):
        print 'File', self.filename
        print 'String #', linenumber
        print string

    def print_string_with_underscore(self, string, tuples, linenumber):
        line = ''
        for tpl in tuples:
            line = line + (" " * (tpl[0] - len(line))) + ('^' * (tpl[1] - tpl[0]))
        print 'File', self.filename
        print 'String #', linenumber
        print string
        print line

    def print_string_in_color(self, string, tuples, linenumber):
        line = ''
        end_of_previous_tuple = 0
        for tpl in tuples:
            line = line + string[end_of_previous_tuple: tpl[0]]
            line = line + string[len(line): tpl[0]]
            line = line + '\033[44;33m' + string[tpl[0]:tpl[1]] + '\033[m'
            end_of_previous_tuple = tpl[1]
        line = line + string[end_of_previous_tuple:]
        print 'File', self.filename
        print 'String #', linenumber
        print line

    def print_string_machine_format(self, string, tuples, linenumber):
        for tpl in tuples:
            print self.filename + ':' + str(linenumber) + ':' + str(tpl[0]) + ':' + string[tpl[0]: tpl[1]]
