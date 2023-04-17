#!/usr/bin/python3
""" base module """
import json
import os
import csv
import turtle


class Base:
    """ create a class named base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return JSON string rep of list_dict """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write JSON string rep of list_objs to file """
        filename = cls.__name__ + ".json"
        if list_objs is None or list_objs == []:
            tlist = "[]"
        else:
            tlist = cls.to_json_string([i.to_dictionary() for i in list_objs])
        with open(filename, 'w') as f:
            f.write(tlist)

        return tlist

    @staticmethod
    def from_json_string(json_string):
        """ return JSON string rep in data list form """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return instance with attributes all set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        tlist = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                m = f.read()
                list_dicts = cls.from_json_string(m)
                for a in list_dicts:
                    tlist.append(cls.create(**d))
        return tlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serialization & save to file """
        if (type(list_objs)) is not list and list_objs is not None or all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [j.to_dictionary() for j in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file(cls):
        """ deserialization from file """
        filename = cls.__name__ + ".csv"
        tlist = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, k in enumerate(row):
                            if k:
                                setattr(i, fields[j], int(k))
                        tlist.append(i)

        return tlist

    @classmethod
    def draw(cls, list_rectangles, list_squares):
        """ opens a window and draws all rectangles and squares """
        window = turtle.Screen()
        pen = turtle.Pen()
        figures = list_rectangles + list_squares

        for fig in figures:
            pen.up()
            pen.goto(fig.x, fig.y)
            pen.down()
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)
            pen.forward(fig.width)
            pen.right(90)
            pen.forward(fig.height)
            pen.right(90)

        window.exitonclick()
