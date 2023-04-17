#!/usr/bin/python3
""" square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ creates a class named square inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ return size """
        return self.width

    @size.setter
    def size(self, size):
        """ get size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ assign attributes """
        tlist = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                    args + tlist[len(args):len(tlist)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return dict rep of square """
        return {'id':self.id, 'x':self.x, 'size':self.size, 'y':self.y}

    def __str(self):
        """ str method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
