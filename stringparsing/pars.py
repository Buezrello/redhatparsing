import re

def getStartEndSubstring(pattern, string):
    return [(a.start(), a.end()) for a in list(re.finditer(pattern, string))]