#!/usr/bin/python3
"""
    class that inherits class list
"""
class MyList(list):
    """
    class MyList that inherits from list
    """

    def print_sorted(self):
        """
        Method that prints sorted list
        """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
