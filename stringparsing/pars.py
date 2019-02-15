import re


class Parsstring:

    def getStartEndSubstring(self, pattern, string):
        return [(a.start(), a.end()) for a in list(re.finditer(pattern, string))]
