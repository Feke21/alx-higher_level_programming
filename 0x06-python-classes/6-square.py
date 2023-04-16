"""Defines a class named Square"""


class Square:
    """Defines a function called __init__"""
    def __init__(self, size):
        """Initializes size of self with size"""
        self.size = size

    @property
    def size(self):
        """Returns __size of self"""
        return self.__size

    @size.setter
    def size(self, value):
        """If statement"""
        if type(value) != int:
            """Raise an error"""
            raise TypeError("size must be an integer")
        elif value < 0:
            """Raise an error"""
            raise ValueError("size must be >= 0")
        else:
            """Initialize __size of self with value"""
            self.__size = value
    @property
    def position(self):
        """Returns __position of self"""
        return self.__position

    @size.setter
    def position(self, value):
        """If statement"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
               raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
