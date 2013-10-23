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
import traceback
from logging import *
from pov.basic.SceneItem import SceneItem
from pov.basic.Vector import Vector
from pov.basic.SceneFile import SceneFile
from pov.basic.BlockObject import BlockObject
from pov.basic.Color import Color
from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.other.IllegalStateException import IllegalStateException


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
        self.SUT = SceneItem('foo', [], [], {'bar': (1, 2, 3), 'baz': SceneItem('bar')})

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
        self.SUT = SceneItem('foo', [1, 2, 3], [4, 5, 6], {'bar': 7})

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
        self.SUT = SceneItem('foo', [1, 2, 3], [4, 5, 6], {'bar': 7})

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

    def test__dedentBelowZero(self):

        try:
            self.SUT._dedent()
        except IllegalStateException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s ' % type(e))
        else:
            self.fail('ExpectedException not thrown')

    def test__validateKwargsInvanildKwarg(self):
        self.SUT = SceneItem('foo', [], [], {'adaptive': (1, 2, 3), 'agate': SceneItem('bar')})

        try:
            self.SUT._validate_kwargs({'boo': 'Vector'})
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s ' % type(e))
        else:
            self.fail('ExpectedException not thrown')

    def test__validateKwargsInvanildKwargValue(self):
        self.SUT = SceneItem('foo', [], [], {'adaptive': (1, 2, 3)})

        try:
            self.SUT._validate_kwargs({'adaptive': 'String'})
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s ' % type(e))
        else:
            self.fail('ExpectedException not thrown')

    def test__is_valid_identifier(self):
        self.assertTrue(self.SUT._is_valid_identifier('foobar'), msg='Valid Identifier')
        self.assertFalse(self.SUT._is_valid_identifier('agate'), msg='Invalid Identifier')

    def test___eq__WrongType(self):
        try:
            if self.SUT == 3:
                pass
        except TypeError:
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

    def test_mul_wrong_type(self):
        try:
            self.SUT * 'foo'
        except SdlSyntaxException as e:
            if not str(e) == 'Parameter not of type float or int':
                self.fail('SdlSyntaxException with wrong message: %s' % str(e))
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_rmul__WrongType(self):
        try:
            'foo' * self.SUT
        except SdlSyntaxException as e:
            if not str(e) == 'Parameter not of type float or int':
                self.fail('SdlSyntaxException with wrong message: %s' % str(e))
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_div__WrongType(self):
        try:
            self.SUT / 'foo'
        except SdlSyntaxException as e:
            if not str(e) == 'Parameter not of type float or int':
                self.fail('SdlSyntaxException with wrong message: %s' % str(e))
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_add__WrongType(self):
        try:
            self.SUT + 'foo'
        except SdlSyntaxException as e:
            if not str(e) == 'Parameter not of type Vector':
                self.fail('SdlSyntaxException with wrong message: %s' % str(e))
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_sub__WrongType(self):
        try:
            self.SUT - 'foo'
        except SdlSyntaxException as e:
            if not str(e) == 'Parameter not of type Vector':
                self.fail('SdlSyntaxException with wrong message: %s' % str(e))
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_dotWrongType(self):
        try:
            self.SUT.dot('foo')
        except SdlSyntaxException as e:
            if not str(e) == 'Parameter not of type Vector':
                self.fail('SdlSyntaxException with wrong message: %s' % str(e))
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')


class SceneFileTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = SceneFile('test.pov', SceneItem('foo'), SceneItem('bar'))

    def tearDown(self):
        self.SUT.close()
        #os.remove(self.SUT.file.name)

    def test_create(self):
        self.assertIsInstance(self.SUT, SceneFile)

    def test_append(self):
        item = SceneItem('baz')
        self.SUT.append(item)

        self.assertIn(item, self.SUT.items)

    def test_createFnamWrongType(self):
        try:
            self.SUT = SceneFile(0, SceneItem('foo'), SceneItem('bar'))
        except TypeError:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('Expected exception not thrown')

    def test_appendWrongType(self):
        try:
            self.SUT.append('foo')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('Expected exception not thrown')

    def test_toString(self):
        le = os.linesep
        first = str(self.SUT)

        second = 'foo {' + le
        second += '}' + le


class BlockObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = BlockObject("foo", [1, 2, 3], [4, 5, 6], {'bar': 7})

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
        self.SUT[4] = BlockObject('bar')

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
        self.SUT= BlockObject('bar')

        self.SUT._indent()
        first = str(self.SUT)
        self.SUT._dedent()

        le = os.linesep

        second = '  bar {' + le
        second += '  }' + le

        self.assertEqual(first, second)


class ColorTestCase(unittest.TestCase):
    '''
        Color Expressions

        COLOR:
            [color] COLOR_BODY | colour COLOR_BODY

        COLOR_BODY:
            COLOR_VECTOR | COLOR_KEYWORD_GROUP | COLOR_IDENTIFIER

        COLOR_VECTOR:
            rgb 3D_VECTOR | rgbf 4D_VECTOR | rgbt 4D_VECTOR | [rgbft] 5D_VECTOR

        COLOR_KEYWORD_GROUP:
            [COLOR_IDENTIFIER] COLOR_KEYWORD_ITEMS

        COLOR_KEYWORD_ITEMS:
            [red FLOAT] & [green FLOAT] & [blue FLOAT] & [filter FLOAT] & [transmit FLOAT]

        @TODO: enable setting color by passing float options e.g. Color(0.0, 0.2, 0.75)
    '''

    def setUp(self):
        self.SUT = Color(rgb=Vector(100, 150, 200))

    def test_create(self):
        self.assertIsInstance(self.SUT, Color)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_CreateRgbColor(self):
        self.assertEqual(self.SUT.type, 'rgb')
        self.assertEqual(self.SUT.vector, Vector(100, 150, 200))

    def test_CreateRgbfColor(self):
        self.SUT = Color(rgbf=Vector(100, 150, 200, 1))
        self.assertEqual(self.SUT.type, 'rgbf')
        self.assertEqual(self.SUT.vector, Vector(100, 150, 200, 1))

    def test_CreateRgbtColor(self):
        self.SUT = Color(rgbt=Vector(100, 150, 200, 2))
        self.assertEqual(self.SUT.type, 'rgbt')
        self.assertEqual(self.SUT.vector, Vector(100, 150, 200, 2))

    def test_CreateRgbftColor(self):
        self.SUT = Color(rgbft=Vector(100, 150, 200, 1, 2))
        self.assertEqual(self.SUT.type, 'rgbft')
        self.assertEqual(self.SUT.vector, Vector(100, 150, 200, 1, 2))

    def test_toStringRGB(self):
        le = os.linesep
        first = str(self.SUT)
        second = 'rgb <100, 150, 200>' + le

        self.assertEqual(first, second)

    def test_mulColor(self):
        self.SUT *= 0.1
        print self.SUT
        self.assertEqual(self.SUT.vector, Vector(10, 15, 20))
