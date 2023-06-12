#!usr/bin/python3
"""
Defines function myList that inherits from list.
"""


class MyList(list):
    """
    Implements sorted printing.
    """

    def print_sorted(self):
        """
        Prints sorted list (ascending).
        """

        print(sorted(self))
