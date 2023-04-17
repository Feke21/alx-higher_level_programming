#!/usr/bin/python3
""" rectangle test module """
import unittest
from models.base import Base
from models.rectangle import Rectangle
import io
import contextlib


class TestRectangle(unittest.TestCase):
    """ create class to test rectangle class """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_0(self):
        """ test zero """
        f = io.StringIO()
