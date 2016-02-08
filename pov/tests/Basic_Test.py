# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

Unittests for basic classes

@SEE: http://docs.python.org/2/library/unittest.html
        #unittest.TestCase.assertRaises
"""

import os
import unittest
from logging import warn
from pov.basic.SceneItem import SceneItem
from pov.basic.Vector import Vector
from pov.basic.SceneFile import SceneFile
from pov.basic.BlockObject import BlockObject
from pov.basic.Color import Color
from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.other.IllegalStateException import IllegalStateException


class SceneItemTestCase(unittest.TestCase):
    """
        Tests for SceneItem class
    """
    def setUp(self):
        """
            Set up fixture
        """
        self.sut = SceneItem('foo')

    def test_creation(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, SceneItem)

    def test_to_string(self):
        """
            Test sut.__str__()
        """
        second = 'foo'
        self.assertEqual(str(self.sut), second)

    def test_append(self):
        """
            Test sut.append()
        """
        second = SceneItem('bar')

        self.sut.append([second])

        self.assertEqual(
            type(self.sut.opts),
            list
        )

        self.assertEqual(
            self.sut.opts,
            [second]
        )

        self.assertIn(
            second,
            self.sut.opts
        )

    def test_append_with_kwarg(self):
        """
            Test sut.append()
        """
        item = SceneItem('bar')
        self.sut.append(baz=item)

        self.assertEqual(
            type(self.sut.kwargs),
            dict
        )

        self.assertEqual(
            self.sut.kwargs,
            {'baz': item}
        )

        self.assertIn(
            'baz',
            self.sut.kwargs
        )

    def test_flatten(self):
        """
            Test sut.flatten()
        """
        first = self.sut.flatten([1, [1, 2], 3, 4])
        self.assertEqual(first, [1, 1, 2, 3, 4])

    def test_create_with_options(self):
        """
            Test creation and inheritance
        """
        self.sut = SceneItem('foo', [], [(1, 2, 3), SceneItem('bar')])

        self.assertEqual(type(self.sut.args), list)
        self.assertEqual(self.sut.args, [])

        self.assertEqual(type(self.sut.opts), list)
        self.assertEqual(
            self.sut.opts,
            [Vector(1, 2, 3), SceneItem('bar')]
        )

        self.assertEqual(type(self.sut.kwargs), dict)
        self.assertEqual(self.sut.kwargs, {})

    def test_create_with_kwargs(self):
        """
            Test creation and inheritance
        """
        self.sut = SceneItem(
            'foo', [], [], {'bar': (1, 2, 3), 'baz': SceneItem('bar')}
        )

        self.assertEqual(type(self.sut.args), list)
        self.assertEqual(self.sut.args, [])

        self.assertEqual(type(self.sut.opts), list)
        self.assertEqual(self.sut.opts, [])

        self.assertEqual(type(self.sut.kwargs), dict)
        self.assertIn('bar', self.sut.kwargs)

        warn(str(Vector(1, 2, 3)))
        warn(str(self.sut.kwargs['bar']))

        self.assertEqual(Vector(1, 2, 3), self.sut.kwargs['bar'])
        self.assertIn('baz', self.sut.kwargs)

        self.assertEqual(SceneItem('bar'), self.sut.kwargs['baz'])

    def test_setitem_replaces_arg(self):
        """
            Test magic method
        """
        self.sut = SceneItem("foo", [SceneItem("bar")])
        other = SceneItem("foo", [SceneItem("baz")])

        self.sut[0] = SceneItem('baz')

        self.assertEqual(
            self.sut,
            other
        )

    def test_setitem_nonexisting_index(self):
        """
            Test magic method
        """
        with self.assertRaisesRegexp(IndexError, ''):
            self.sut[2] = SceneItem('baz')

    def test_block_end_zero_indentation(self):
        """
            Test pseudo private method
        """
        self.assertEqual(self.sut._block_end(), os.linesep)

    def test_setitem_replaces_opt(self):
        """
            Test magic method
        """
        self.sut = SceneItem('foo', [1, 2, 3], [4, 5, 6], {'bar': 7})

        # before
        self.assertEqual(self.sut.args, [1, 2, 3])
        self.assertEqual(self.sut.opts, [4, 5, 6])
        self.assertEqual(self.sut.kwargs, {'bar': 7})

        self.sut[4] = 0

        # after
        self.assertEqual(self.sut.args, [1, 2, 3])
        self.assertEqual(self.sut.opts, [4, 0, 6])
        self.assertEqual(self.sut.kwargs, {'bar': 7})

    def test_getitem(self):
        """
            Test magic method
        """
        self.sut = SceneItem('foo', [1, 2, 3], [4, 5, 6], {'bar': 7})

        self.assertEqual(self.sut[1], 2)
        self.assertEqual(self.sut[4], 5)

    def test_getitem_raises_index_error(self):
        """
            Test magic method
        """
        with self.assertRaisesRegexp(IndexError, ''):
            warn(str(self.sut[2]))

    def test__dedent_below_zero(self):
        """
            Test pseudo private method
        """
        with self.assertRaisesRegexp(
            IllegalStateException, 'Indentation below zero'
        ):
            self.sut._dedent()

    def test__validate_kwargs_invanild_kwarg(self):
        """
            Test pseudo private method
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Keyword agate not allowed for object SceneItem'
        ):
            self.sut = SceneItem(
                'foo', [], [],
                {'adaptive': (1, 2, 3), 'agate': SceneItem('bar')}
            )
            self.sut._validate_kwargs({'boo': 'Vector'})

    def test__validate_kwargs_invanild_kwarg_type(self):
        """
            Test pseudo private method
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            ' '.join([
                'Value of KW Argument adaptive is expectet',
                'to be type String but got Vector'
            ])
        ):
            self.sut = SceneItem('foo', [], [], {'adaptive': (1, 2, 3)})
            self.sut._validate_kwargs({'adaptive': 'String'})

    def test__is_valid_identifier(self):
        """
            Test pseudo private method
        """
        self.assertTrue(
            self.sut._is_valid_identifier('foobar'), msg='Valid Identifier'
        )
        self.assertFalse(
            self.sut._is_valid_identifier('agate'), msg='Invalid Identifier'
        )

    def test___eq__wrong_type(self):
        """
            Test magic method
        """
        with self.assertRaisesRegexp(
            TypeError,
            'can only be compared to objects of same type'
        ):
            if self.sut == 3:
                pass

    def test__check_kwarg_value_invalid_value(self):
        """
            Test pseudo private method
        """
        self.sut = SceneItem('foo', [], [], {'baz': 'bar'})

        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Value of KW Argument baz is expectet to be in .* but got bar'
        ):
            self.sut._checkKwargValue('baz', ['foo'])


class VectorTestCase(unittest.TestCase):
    """
        Tests for Vector class
    """
    def setUp(self):
        """
            Set up fixture
        """
        self.sut = Vector(1, 2, 3)

    def test_create(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, Vector)

    def test_create_with_vector(self):
        """
            Test creation and inheritance
        """
        self.sut = Vector(Vector(1, 2, 3))
        self.assertIsInstance(self.sut, Vector)

    def test_repr(self):
        """
            Test magic method
        """
        self.assertEqual(repr(self.sut), "Vector(1, 2, 3)")

    def test_equals(self):
        """
            Test magic method
        """
        self.assertEqual(self.sut, Vector(1, 2, 3))

    def test_equals_no_vector(self):
        """
            Test magic method
        """
        self.assertNotEqual(self.sut, SceneItem('bar'))

    def test_setattr(self):
        """
            Test magic method
        """
        self.sut[1] = 4
        self.assertEqual(self.sut, Vector(1, 4, 3))

    def test_getattr(self):
        """
            Test magic method
        """
        self.assertEqual(self.sut[1], 2)

    def test_mul(self):
        """
            Test magic method
        """
        self.assertEqual(self.sut * 2, Vector(2, 4, 6))

    def test_rmul(self):
        """
            Test magic method
        """
        self.assertEqual(2 * self.sut, Vector(2, 4, 6))

    def test_div(self):
        """
            Test magic method
        """
        self.assertEqual(Vector(2, 4, 6) / 2, Vector(1, 2, 3))

    def test_add(self):
        """
            Test magic method
        """
        self.assertEqual(self.sut + self.sut, Vector(2, 4, 6))

    def test_sub(self):
        """
            Test magic method
        """
        self.assertEqual(Vector(2, 4, 6) - self.sut, self.sut)

    def test_neg(self):
        """
            Test magic method
        """
        self.assertEqual(-self.sut, Vector(-1, -2, -3))

    def test_norm(self):
        """
            Test sut.norm()
        """
        self.sut = Vector(1, 2, 2)
        self.assertEqual(self.sut.norm(), 3)

    def test_normalize(self):
        """
            Test sut.normalize()
        """
        self.sut = Vector(1, 2, 2)
        self.assertEqual(self.sut.normalize(), Vector(1.0 / 3, 2.0 / 3, 2.0 / 3))

    def test_dot(self):
        """
            Test sut.dot()
        """
        self.assertEqual(self.sut.dot(self.sut), 14)

    def test_mul_wrong_type(self):
        """
            Test magic method
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Parameter not of type float or int'
        ):
            self.sut * 'foo'

    def test_rmul__wrong_type(self):
        """
            Test magic method
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter not of type float or int'
        ):
            'foo' * self.sut

    def test_div__wrong_type(self):
        """
            Test magic method
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter not of type float or int'
        ):
            self.sut / 'foo'

    def test_add__wrong_type(self):
        """
            Test magic method
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter not of type Vector'
        ):
            self.sut + 'foo'

    def test_sub__wrong_type(self):
        """
            Test magic method
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Parameter not of type Vector'
        ):
            self.sut - 'foo'

    def test_dot_wrong_type(self):
        """
            Test sut.dot()
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter not of type Vector'
        ):
            self.sut.dot('foo')


class SceneFileTestCase(unittest.TestCase):
    """
        Tests for SceneFile class
    """
    def setUp(self):
        """
            Set up fixture
        """
        self.sut = SceneFile('test.pov', SceneItem('foo'), SceneItem('bar'))

    def tearDown(self):
        """
            Cleanup after tests
        """
        self.sut.close()
        # os.remove(self.sut.file.name)

    def test_create(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, SceneFile)

    def test_append(self):
        """
            Test sut.append()
        """
        item = SceneItem('baz')
        self.sut.append(item)

        self.assertIn(item, self.sut.items)

    def test_create_fnam_wrong_type(self):
        """
            Test creation and inheritance
        """
        with self.assertRaisesRegexp(
            TypeError, 'Filename String expected but got int'
        ):
            self.sut = SceneFile(0, SceneItem('foo'), SceneItem('bar'))

    def test_append_wrong_type(self):
        """
            Test sut.append()
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Item is expectet to be a SceneItem object but got str'
        ):
            self.sut.append('foo')

    def test_to_string(self):
        """
            Test sut.__str__()
        """
        first = str(self.sut)

        second = 'foo {' + os.linesep
        second += '}' + os.linesep

        # @TODO: No Assertion!


class BlockObjectTestCase(unittest.TestCase):
    """
        @Todo: DocString
    """
    def setUp(self):
        """
            Set up fixture
        """
        self.sut = BlockObject("foo", [1, 2, 3], [4, 5, 6], {'bar': 7})

    def test_to_string(self):
        """
            Test sut.__str__()
        """
        first = str(self.sut)
        second = 'foo {' + os.linesep
        second += '  1, 2, 3' + os.linesep
        second += '  4' + os.linesep
        second += '  5' + os.linesep
        second += '  6' + os.linesep
        second += '  bar 7' + os.linesep
        second += '}' + os.linesep

        self.assertEqual(first, second)

    def test_to_string_with_object_option(self):
        """
            Test sut.__str__()
        """
        self.sut[4] = BlockObject('bar')

        first = str(self.sut)
        second = 'foo {' + os.linesep
        second += '  1, 2, 3' + os.linesep
        second += '  4' + os.linesep
        second += '  bar {' + os.linesep
        second += '  }' + os.linesep
        second += '  6' + os.linesep
        second += '  bar 7' + os.linesep
        second += '}' + os.linesep

        self.assertEqual(first, second)

    def test_to_string_with_indent(self):
        """
            Test sut.__str__()
        """
        self.sut = BlockObject('bar')

        self.sut._indent()
        first = str(self.sut)
        self.sut._dedent()

        second = '  bar {' + os.linesep
        second += '  }' + os.linesep

        self.assertEqual(first, second)


class ColorTestCase(unittest.TestCase):
    """
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
            [red FLOAT] & [green FLOAT] & [blue FLOAT]
            & [filter FLOAT] & [transmit FLOAT]

        @TODO: enable setting color by passing float
               options e.g. Color(0.0, 0.2, 0.75)
    """

    def setUp(self):
        """
            Set up fixture
        """
        self.sut = Color(rgb=Vector(100, 150, 200))

    def test_create(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, Color)
        self.assertIsInstance(self.sut, SceneItem)

    def test_create_rgb_color(self):
        """
            Test creation and inheritance
        """
        self.assertEqual(self.sut.type, 'rgb')
        self.assertEqual(self.sut.vector, Vector(100, 150, 200))

    def test_create_rgbf_color(self):
        """
            Test creation and inheritance
        """
        self.sut = Color(rgbf=Vector(100, 150, 200, 1))
        self.assertEqual(self.sut.type, 'rgbf')
        self.assertEqual(self.sut.vector, Vector(100, 150, 200, 1))

    def test_create_rgbt_color(self):
        """
            Test creation and inheritance
        """
        self.sut = Color(rgbt=Vector(100, 150, 200, 2))
        self.assertEqual(self.sut.type, 'rgbt')
        self.assertEqual(self.sut.vector, Vector(100, 150, 200, 2))

    def test_create_rgbft_color(self):
        """
            Test creation and inheritance
        """
        self.sut = Color(rgbft=Vector(100, 150, 200, 1, 2))
        self.assertEqual(self.sut.type, 'rgbft')
        self.assertEqual(self.sut.vector, Vector(100, 150, 200, 1, 2))

    def test_to_string_rgb(self):
        """
            Test sut.__str__()
        """
        lsp = os.linesep
        first = str(self.sut)
        second = 'color rgb <100, 150, 200>' + lsp

        self.assertEqual(first, second)

    def test_mul_color(self):
        """
            Test sut.__mul__()
        """
        self.sut *= 0.1
        print self.sut
        self.assertEqual(self.sut.vector, Vector(10, 15, 20))

    def test_color_return_type(self):
        """Test for color type."""
        self.sut = Color(rgb=Vector(33 / 255.0, 33 / 255.0, 33 / 255.0))
        self.assertEqual(type(self.sut), tuple)
