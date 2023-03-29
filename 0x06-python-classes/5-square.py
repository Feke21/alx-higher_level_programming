"""Defines a class named Square"""


class Square:
    """Defines a function called __init__"""
    def __init__(self, size=0):
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
    """Defines area function or public instance method"""
    def area(self):
        """Returns area"""
        return self.__size ** 2
    """Defines a print function"""
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
