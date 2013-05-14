# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Unittests for basic classes

"""

import os
import unittest
#import difflib
#import copy
from logging import *
from pov.basic import *


class SceneItemTestCase(unittest.TestCase):

    def setUp(self):
        self.SUT = SceneItem('foo')

    def test_creation(self):
        self.assertIsInstance(self.SUT, SceneItem)

    def test_toString(self):
        second = 'foo'

        self.assertEqual(str(self.SUT), second)

    def test_append(self):
        second = SceneItem('bar')

        self.SUT.append([second])

        self.assertEqual(
            type(self.SUT.opts),
            list
        )

        self.assertEqual(
            self.SUT.opts,
            [second]
        )

        self.assertIn(
            second,
            self.SUT.opts
        )

    def test_appendWithKwarg(self):
        item = SceneItem('bar')
        self.SUT.append(baz=item)

        self.assertEqual(
            type(self.SUT.kwargs),
            dict
        )

        self.assertEqual(
            self.SUT.kwargs,
            {'baz': item}
        )

        self.assertIn(
            'baz',
            self.SUT.kwargs
        )

    def test_flatten(self):
        first = self.SUT.flatten([1, [1, 2], 3, 4])
        self.assertEqual(first, [1, 1, 2, 3, 4])

    def test_createWithOptions(self):
        self.SUT = SceneItem('foo', [], [(1, 2, 3), SceneItem('bar')])

        self.assertEqual(type(self.SUT.args), list)
        self.assertEqual(self.SUT.args, [])

        self.assertEqual(type(self.SUT.opts), list)
        self.assertEqual(
            self.SUT.opts,
            [Vector(1, 2, 3), SceneItem('bar')]
        )

        self.assertEqual(type(self.SUT.kwargs), dict)
        self.assertEqual(self.SUT.kwargs, {})

    def test_createWithKwargs(self):
        self.SUT = SceneItem('foo', [], [], bar=(1, 2, 3),  baz=SceneItem('bar'))

        self.assertEqual(type(self.SUT.args), list)
        self.assertEqual(self.SUT.args, [])

        self.assertEqual(type(self.SUT.opts), list)
        self.assertEqual(self.SUT.opts, [])

        self.assertEqual(type(self.SUT.kwargs), dict)
        self.assertIn('bar', self.SUT.kwargs)

        warn(str(Vector(1, 2, 3)))
        warn(str(self.SUT.kwargs['bar']))

        self.assertEqual(Vector(1, 2, 3), self.SUT.kwargs['bar'])
        self.assertIn('baz', self.SUT.kwargs)

        self.assertEqual(SceneItem('bar'), self.SUT.kwargs['baz'])

    def test_setitemReplacesArg(self):
        self.SUT = SceneItem("foo", [SceneItem("bar")])
        other = SceneItem("foo", [SceneItem("baz")])

        self.SUT[0] = SceneItem('baz')

        self.assertEqual(
            self.SUT,
            other
        )

    def test_setitemNonexistingIndex(self):
        try:
            self.SUT[2] = SceneItem('baz')
        except IndexError:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s ' % type(e))
        else:
            self.fail('ExpectedException not thrown')

    def test_block_endZeroIndentation(self):
        self.assertEqual(self.SUT._block_end(), os.linesep)

    def test_setitemReplacesOpt(self):
        self.SUT = SceneItem('foo', [1, 2, 3], [4, 5, 6], bar=7)

        #before
        self.assertEqual(self.SUT.args, [1, 2, 3])
        self.assertEqual(self.SUT.opts, [4, 5, 6])
        self.assertEqual(self.SUT.kwargs, {'bar': 7})

        self.SUT[4] = 0

        #after
        self.assertEqual(self.SUT.args, [1, 2, 3])
        self.assertEqual(self.SUT.opts, [4, 0, 6])
        self.assertEqual(self.SUT.kwargs, {'bar': 7})

    def test_getitem(self):
        self.SUT = SceneItem('foo', [1, 2, 3], [4, 5, 6], bar=7)

        self.assertEqual(self.SUT[1], 2)
        self.assertEqual(self.SUT[4], 5)

    def test_getitemRaisesIndexError(self):
        try:
            warn(str(self.SUT[2]))
        except IndexError:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s ' % type(e))
        else:
            self.fail('ExpectedException not thrown')


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

    def test_equalsNoVector(self):
        self.assertNotEqual(self.SUT, SceneItem('bar'))

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
        self.assertEqual(SUT.normalize(), Vector(1.0 / 3, 2.0 / 3, 2.0 / 3))

    def test_dot(self):
        self.assertEqual(self.SUT.dot(self.SUT), 14)


class SceneFileTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = SceneFile('test.pov', SceneItem('foo'), SceneItem('bar'))

    def tearDown(self):
        self.SUT.close()
        os.remove(self.SUT.file.name)

    def test_create(self):
        self.assertIsInstance(self.SUT, SceneFile)

    def test_append(self):
        item = SceneItem('baz')
        self.SUT.append(item)

        self.assertIn(item, self.SUT.items)

    def test_appendWrongType(self):
        try:
            self.SUT.append('foo')
        except TypeError:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_toString(self):
        le = os.linesep
        first = str(self.SUT)

        second = 'foo {' + le
        second += '}' + le


class PoVObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = PoVObject("foo", [1, 2, 3], [4, 5, 6], bar=7)

    def test_toString(self):
        le = os.linesep
        first = str(self.SUT)
        second = 'foo {' + le
        second += '  1, 2, 3' + le
        second += '  4' + le
        second += '  5' + le
        second += '  6' + le
        second += '  bar 7' + le
        second += '}' + le

        self.assertEqual(first, second)

    def test_toString_with_object_option(self):
        self.SUT[4] = PoVObject('bar')

        le = os.linesep
        first = str(self.SUT)
        second = 'foo {' + le
        second += '  1, 2, 3' + le
        second += '  4' + le
        second += '  bar {' + le
        second += '  }' +le
        second += '  6' + le
        second += '  bar 7' + le
        second += '}' + le

        self.assertEqual(first, second)

    def test_toString_with_indent(self):
        self.SUT= PoVObject('bar')

        self.SUT._indent()
        first = str(self.SUT)
        self.SUT._dedent()

        le = os.linesep

        second = '  bar {' + le
        second += '  }' + le

        self.assertEqual(first, second)