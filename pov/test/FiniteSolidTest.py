# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

import os
import unittest

from pov.other.SdlSyntaxException import SdlSyntaxException
from pov.basic.PoVObject import PoVObject
from pov.basic.Vector import Vector
from pov.basic.SceneItem import SceneItem
from pov.object_modifier.ObjectModifier import ObjectModifier

from pov.finite_solid.Blob import Blob
from pov.finite_solid.Box import Box
from pov.finite_solid.Cone import Cone
from pov.finite_solid.Cylinder import Cylinder
from pov.finite_solid.HeightField import HeightField
from pov.finite_solid.JuliaFractal import JuliaFractal



class BlobTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Blob()

    def test_create(self):
        self.assertIsInstance(self.SUT, Blob)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'blob {' + le + '}' + le

        self.assertEqual(str(self.SUT), second)


class BoxTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = Box(Vector(1, 2, 3), Vector(4, 5, 6))

    def test_create(self):
        self.assertIsInstance(self.SUT, Box)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'box {' + le
        second += '  <1, 2, 3>, <4, 5, 6>' + le
        second += '}' + le

        self.assertEqual(
            str(self.SUT),
            second
        )

    def test_createWithOption(self):
        SUT = Box(Vector(1, 2, 3), Vector(4, 5, 6), ObjectModifier('foo'))

        self.assertIsInstance(SUT, Box)
        self.assertIsInstance(SUT, SceneItem)

    def test_create_v1_wrong_type(self):
        try:
            self.SUT = Box(
                'foo',
                Vector(5, 6, 7),
                ObjectModifier('foo')
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_v2_wrong_type(self):
        try:
            self.SUT = Box(
                Vector(5, 6, 7),
                'foo',
                ObjectModifier('foo')
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_v1_wrong_length(self):
        try:
            self.SUT = Box(
                Vector(1, 2),
                Vector(5, 6, 7),
                ObjectModifier('foo')
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_v2_wrong_length(self):
        try:
            self.SUT = Box(
                Vector(1, 2, 3),
                Vector(4, 5, 6, 7),
                ObjectModifier('foo')
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_option_wrong_length(self):
        try:
            self.SUT = Box(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                Vector(1, 2)
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')


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
        second = 'cone {' + le
        second += '  <1, 2, 3>, 4, <5, 6, 7>, 8' + le
        second += '}' + le

        self.assertEqual(
            str(self.SUT),
            second
        )

    def test_creationWithOptionAndKwarg(self):
        self.SUT = Cone(
            Vector(1, 2, 3),
            4,
            Vector(5, 6, 7),
            8,
            ObjectModifier('foo'),
            open=True
        )

        self.assertIsInstance(self.SUT, Cone)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_create_non_existant_kw(self):
        try:
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                foo=True
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_open_wrong_type(self):
        try:
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_baseradius_wrong_type(self):
        try:
            self.SUT = Cone(
                Vector(1, 2, 3),
                'foo',
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_capradius_wrong_type(self):
        try:
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                'foo',
                ObjectModifier('foo'),
                open=0.3
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_option_wrong_type(self):
        try:
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                Vector(1, 2),
                open=0.3
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')


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
        second = 'cylinder {' + le
        second += '  <1, 2, 3>, <5, 6, 7>, 8' + le
        second += '}' + le

        self.assertEqual(
            str(self.SUT),
            second
        )

    def test_creationWithOptionAndKwarg(self):
        self.SUT = Cylinder(
            Vector(1, 2, 3),
            Vector(5, 6, 7),
            8,
            ObjectModifier('foo'),
            open=True
        )

        self.assertIsInstance(self.SUT, Cylinder)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_create_non_existant_kw(self):
        try:
            self.SUT = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                bar=True
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_open_wrong_type(self):
        try:
            self.SUT = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open='foo'
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')


class HeightFieldTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = HeightField('foo.gif')

    def test_creation(self):
        self.assertIsInstance(self.SUT, HeightField)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_create_wrong_type(self):
        try:
            self.SUT = HeightField(1.0)
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_Vector_wrong_option(self):
        try:
            self.SUT = HeightField('foo', Vector(1, 2, 3, 4))
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_non_existant_kw(self):
        try:
            self.SUT = HeightField('baz', foo='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_smooth_wrong_type(self):
        try:
            self.SUT = HeightField('baz', smooth='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_hierarchy_wrong_type(self):
        try:
            self.SUT = HeightField('baz', hierarchy='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_hf_type_wrong_type(self):
        try:
            self.SUT = HeightField('baz', hf_type=0.2)
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_hf_type_non_existant_value(self):
        try:
            self.SUT = HeightField('baz', hf_type='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_waterlevel_not_float(self):
        try:
            self.SUT = HeightField('baz', water_level='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')


class JuliaFractalTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = JuliaFractal(Vector(1, 2, 3, 4))

    def test_creation(self):
        self.assertIsInstance(self.SUT, JuliaFractal)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_create_wrong_type(self):
        try:
            self.SUT = JuliaFractal('foo')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_Vector_wrong_dimension(self):
        try:
            self.SUT = JuliaFractal(Vector(1, 2))
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_Vector_wrong_option(self):
        try:
            self.SUT = JuliaFractal(Vector(1, 2, 3, 4), Vector(1, 2, 3, 4))
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_non_existant_kw(self):
        try:
            self.SUT = JuliaFractal(Vector(1, 2, 3, 4), foo='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' % (type(e), str(e)))
        else:
            self.fail('ExpectedException not thrown')
