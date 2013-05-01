"""
    Unittests File
"""

import unittest
from SceneItem import *
from PoVObject import *
from Vector import *


class SceneItemTest(unittest.TestCase):

    def setUp(self):
        self.SUT = SceneItem('foo')

    def test_creation(self):
        self.assertIsInstance(self.SUT, SceneItem)

    def test_toString(self):
        self.assertEqual(str(self.SUT), 'foo\r\n  {\r\n  }\r\n')

    def test_append(self):
        self.SUT.append(SceneItem('foo'))
        self.assertEqual(str(self.SUT), 'foo\r\n  {\r\n  foo\r\n    {\r\n    }\r\n  }\r\n')

    #TODO: test map_arg

    def test_flatten(self):
        first = self.SUT.flatten([1, [1, 2], 3, 4])
        self.assertEqual(first, [1, 1, 2, 3, 4])


class BlobTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Blob()

    def test_create(self):
        self.assertIsInstance(self.SUT, Blob)
        self.assertIsInstance(self.SUT, SceneItem)
        self.assertEqual(str(self.SUT), 'blob\r\n  {\r\n  }\r\n')


class BoxTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Box(Vector(1, 2, 3), Vector(4, 5, 6))

    def test_create(self):
        self.assertIsInstance(self.SUT, Box)
        self.assertIsInstance(self.SUT, SceneItem)
        self.assertEqual(
            str(self.SUT),
            'box\r\n  {\r\n  <1, 2, 3>, <4, 5, 6>\r\n  }\r\n'
        )


class ConeTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Cone(
            Vector(1, 2, 3),
            4,
            Vector(5, 6, 7),
            8
        )

    def test_creation(self):
        self.assertIsInstance(self.SUT, Cone)
        self.assertIsInstance(self.SUT, SceneItem)
        self.assertEqual(
            str(self.SUT),
            'cone\r\n  {\r\n  <1, 2, 3>, 4, <5, 6, 7>, 8\r\n  }\r\n'
        )


if __name__ == '__main__':
    unittest.main()
