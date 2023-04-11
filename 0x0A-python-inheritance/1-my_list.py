#!/usr/bin/python3
""" my_list module """


class MyList(list):
    """ MyList is a child class of parent class list """
    def print_sorted(self):
        """ prints the list in sorted form (ascending order) """
        print(sorted(self))
