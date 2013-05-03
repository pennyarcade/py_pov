"""
    Unittests File
"""

import os
import unittest
import difflib
from SceneItem import *
from PoVObject import *
from Vector import *


class SceneItemTest(unittest.TestCase):

    def setUp(self):
        self.SUT = SceneItem('foo')

    def test_creation(self):
        self.assertIsInstance(self.SUT, SceneItem)

    def test_toString(self):
        le = os.linesep
        second = 'foo' + le + '  {' + le + '  }' + le

        self.assertEqual(str(self.SUT), second)

    def test_append(self):
        self.SUT.append(SceneItem('bar'))

        le = os.linesep
        second = 'foo' + le + '  {' + le
        second += '  bar' + le + '    {' + le + '    }' + le + '' + le
        second += '  }' + le

        msg = "Strings not Equal:" + le + ''.join(
            difflib.ndiff(
                str(self.SUT).splitlines(1),
                second.splitlines(1)
            )
        )

        self.assertEqual(
            str(self.SUT),
            second,
            msg
        )

    def test_appendWithKwarg(self):
        self.SUT.append(baz=SceneItem('bar'))

        le = os.linesep
        second = 'foo' + le + '  {' + le
        second += '  baz bar' + le + '    {' + le + '    }' + le + '' + le
        second += '  }' + le

        msg = "Strings not Equal:" + le + ''.join(
            difflib.ndiff(
                str(self.SUT).splitlines(1),
                second.splitlines(1)
            )
        )

        self.assertEqual(
            str(self.SUT),
            second,
            msg
        )

    def test_flatten(self):
        first = self.SUT.flatten([1, [1, 2], 3, 4])
        self.assertEqual(first, [1, 1, 2, 3, 4])

    def test_createWithOptions(self):
        self.SUT = SceneItem('foo', [], [(1, 2, 3), SceneItem('bar')])

        le = os.linesep
        second = 'foo' + le + '  {' + le
        second += '  <1, 2, 3>' + le
        second += '  bar' + le + '    {' + le + '    }' + le + le
        second += '  }' + le

        msg = "Strings not Equal:" + le + ''.join(
            difflib.unified_diff(
                str(self.SUT).splitlines(1),
                second.splitlines(1)
            )
        )

        self.assertEqual(str(self.SUT), second, msg)

    def test_createWithKwargs(self):
        self.SUT = SceneItem('foo', [], [], bar=(1, 2, 3),  baz=SceneItem('bar'))

        le = os.linesep
        second = 'foo' + le + '  {' + le
        second += '  bar <1, 2, 3>' + le
        second += '  baz bar' + le + '    {' + le + '    }' + le + le
        second += '  }' + le

        msg = "Strings not Equal:" + le + ''.join(
            difflib.ndiff(
                str(self.SUT).splitlines(1),
                second.splitlines(1)
            )
        )

        self.assertEqual(str(self.SUT), second, msg)

    def test_setitemReplacesArg(self):
        self.SUT = SceneItem("foo", [SceneItem("bar")])

        le = os.linesep
        second = 'foo' + le + '  {' + le
        second += '  bar' + le + '    {' + le + '    }' + le + '' + le
        second += '  }' + le

        msg = "Strings not Equal:" + le + ''.join(
            difflib.ndiff(
                str(self.SUT).splitlines(1),
                second.splitlines(1)
            )
        )

        self.assertEqual(
            str(self.SUT),
            second,
            msg
        )

        self.SUT[0] = SceneItem('baz')

        le = os.linesep
        second = 'foo' + le + '  {' + le
        second += '  baz' + le + '    {' + le + '    }' + le + '' + le
        second += '  }' + le

        msg = "Strings not Equal:" + le + ''.join(
            difflib.ndiff(
                str(self.SUT).splitlines(1),
                second.splitlines(1)
            )
        )

        self.assertEqual(
            str(self.SUT),
            second,
            msg
        )

    def test_setitemNonexistingIndex(self):
        self.SUT[2] = SceneItem('baz')

        le = os.linesep
        second = 'foo' + le + '  {' + le
        second += '  }' + le

        msg = "Strings not Equal:" + le + ''.join(
            difflib.ndiff(
                str(self.SUT).splitlines(1),
                second.splitlines(1)
            )
        )

        self.assertEqual(
            str(self.SUT),
            second,
            msg
        )


class BlobTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Blob()

    def test_create(self):
        self.assertIsInstance(self.SUT, Blob)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'blob' + le + '  {' + le + '  }' + le

        self.assertEqual(str(self.SUT), second)


class BoxTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Box(Vector(1, 2, 3), Vector(4, 5, 6))

    def test_create(self):
        self.assertIsInstance(self.SUT, Box)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'box' + le + '  {' + le
        second += '  <1, 2, 3>, <4, 5, 6>' + le + '  }' + le

        self.assertEqual(
            str(self.SUT),
            second
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

        le = os.linesep
        second = 'cone' + le + '  {' + le
        second += '  <1, 2, 3>, 4, <5, 6, 7>, 8' + le + '  }' + le

        self.assertEqual(
            str(self.SUT),
            second
        )


class CylinderTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Cylinder(
            Vector(1, 2, 3),
            Vector(5, 6, 7),
            8
        )

    def test_creation(self):
        self.assertIsInstance(self.SUT, Cylinder)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'cylinder' + le + '  {' + le
        second += '  <1, 2, 3>, <5, 6, 7>, 8' + le + '  }' + le

        self.assertEqual(
            str(self.SUT),
            second
        )


class VectorTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Vector(1, 2, 3)

    def test_create(self):
        self.assertIsInstance(self.SUT, Vector)

    def test_createWithVector(self):
        self.SUT = Vector(Vector(1, 2, 3))
        self.assertIsInstance(self.SUT, Vector)

    def test_repr(self):
        self.assertEqual(repr(self.SUT), "Vector(1, 2, 3)")

    def test_equals(self):
        self.assertEqual(self.SUT, Vector(1, 2, 3))

    def test_setattr(self):
        self.SUT[1] = 4
        self.assertEqual(self.SUT, Vector(1, 4, 3))

    def test_getattr(self):
        self.assertEqual(self.SUT[1], 2)

    def test_mul(self):
        self.assertEqual(self.SUT * 2, Vector(2, 4, 6))

    def test_rmul(self):
        self.assertEqual(2 * self.SUT, Vector(2, 4, 6))

    def test_div(self):
        self.assertEqual(Vector(2, 4, 6) / 2, Vector(1, 2, 3))

    def test_add(self):
        self.assertEqual(self.SUT + self.SUT, Vector(2, 4, 6))

    def test_sub(self):
        self.assertEqual(Vector(2, 4, 6) - self.SUT, self.SUT)

    def test_neg(self):
        self.assertEqual(-self.SUT, Vector(-1, -2, -3))

    def test_norm(self):
        SUT = Vector(1, 2, 2)
        self.assertEqual(SUT.norm(), 3)

    def test_normalize(self):
        SUT = Vector(1, 2, 2)
        third = 1 / 3
        self.assertEqual(SUT.normalize(), Vector(third, (2 / 3), (2 / 3)))


if __name__ == '__main__':
    unittest.main()
