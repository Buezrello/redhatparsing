import re


class Parsstring:
    """
    A class used for pattern matching

    Methods
    -------
        __init__()
            Class initialization withot parameters

        getStartEndSubstring(self, pattern, string)
            Method searches pattern(s) in a string and return tuple
            with (start, end) indexes
    """

    def __init__(self):
        """
        Create class object without parameters
        """

        pass

    def getStartEndSubstring(self, pattern, string):
        """
        :param pattern: str
            regex pattern
        :param string: str
            string for pattern searching
        :return: tuple(int, int)
            start and end of pattern in the string

        Attributes
        ----------
            pattern : str
                regex
            string : str
                string for pattern searching

        Return
        ------
            tuple with (start, end) index
        """

        return [(a.start(), a.end()) for a in list(re.finditer(pattern, string))]
