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
import traceback

from pov.other.SdlSyntaxException import SdlSyntaxException
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
    '''
        BLOB:
            blob { BLOB_ITEM... [BLOB_MODIFIERS...]}
        BLOB_ITEM:
            sphere{<Center>, Radius,
                   [ strength ] Strength[COMPONENT_MODIFIER...] } |
            cylinder{<End1>, <End2>, Radius,
                     [ strength ] Strength [COMPONENT_MODIFIER...] } |
            component Strength, Radius, <Center> |
            threshold Amount
        COMPONENT_MODIFIER:
            TEXTURE | PIGMENT | NORMAL | FINISH | TRANSFORMATION
        BLOB_MODIFIER:
            hierarchy [Boolean] | sturm [Boolean] | OBJECT_MODIFIER
    '''

    def setUp(self):
        self.SUT = Blob()

    def test_create(self):
        self.assertIsInstance(self.SUT, Blob)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'blob {' + le + '}' + le

        self.assertEqual(str(self.SUT), second)


class BoxTestCase(unittest.TestCase):
    '''
        BOX:
            box
            {
                <Corner_1>, <Corner_2>
                [OBJECT_MODIFIERS...]
            }

        OBJECT_MODIFIERS:
            [OBJECT_PHOTONS] |
            [CLIPPED_BY] |
            [BOUNDED_BY] |
            [MATERIAL] |
            [INTERIOR] |
            [INTERIOR_TEXTURE] |
            [TEXTURE] |
            [PIGMENT] |
            [NORMAL] |
            [FINISH] |
            [TRANSFORMATION...] |

            [no_shadow] |
            [no_image[BOOL]] |
            [no_reflection{BOOL]] |
            [inverse] |
            [double_illuminate[BOOL]] |
            [hollow [BOOL]]

        OBJECT_PHOTONS:
            photons { OBJECT_PHOTON_ITEMS }

        CLIPPED_BY:
            clipped_by { UNTEXTURED_SOLID_OBJECT... } |
            clipped_by { bounded_by }

        MATERIAL:
            material { [MATERIAL_IDENTIFIER] [MATERIAL_ITEM ...] }

        INTERIOR:
            interior { [INTERIOR_IDENTIFIER] [INTERIOR_ITEMS] }

        INTERIOR_TEXTURE:
            interior_texture { TEXTURE_BODY }

        TEXTURE:
            texture { TEXTURE_BODY }

        PIGMENT:
            pigment { PIGMENT_BODY }

        NORMAL:
            normal { NORMAL_BODY }

        FINISH:
            finish { [FINISH_IDENTIFIER] [FINISH_ITEMS] }

        TRANSFORMATION:
            rotate VECTOR | scale VECTOR | translate VECTOR | TRANSFORM | MATRIX
            TRANSFORM:
            transform TRANSFORM_IDENTIFIER | transform { [TRANSFORM_ITEM...] }

        MATRIX:
            matrix < F_VAL00, F_VAL01, F_VAL02,
                     F_VAL10, F_VAL11, F_VAL12,
                     F_VAL20, F_VAL21, F_VAL22,
                     F_VAL30, F_VAL31, F_VAL32 >

        Rules to Check:
            @ToDo: KwArg: 0..1 no_shadow Bool
            @ToDo: KwArg: 0..1 no_image Bool
            @ToDo: KwArg: 0..1 no_reflection BOOL
            @ToDo: KwArg: 0..1 inverse bool
            @ToDo: KwArg: 0..1 double_illuminate bool
            @ToDo: KwArg: 0..1 hollow bool
            @ToDo: KwArg: 0..1 rotate Vector 3D
            @ToDo: KwArg: 0..1 scale Vector 3D
            @ToDo: KwArg: 0..1 translate Vector 3D
            @ToDo: KwArg: 0..1 matrix Vector 12D

            @ToDo: Option: 0..1 Photon object
            @ToDo: Option: 0..1 clipped_by object
            @ToDo: Option: 0..1 material object
            @ToDo: Option: 0..1 interior object
            @ToDo: Option: 0..1 interior_texture object
            @ToDo: Option: 0..1 texture object
            @ToDo: Option: 0..1 pigment object
            @ToDo: Option: 0..1 normal object
            @ToDo: Option: 0..1 finish object

            @ToDo: Option: 0..1 transform object
            @ToDo: KwArg: 0..1 transform string; existing identifier; transform object
            @ToDo: only one "transform"
    '''

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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_option_wrong_type(self):
        try:
            self.SUT = Box(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                Vector(1, 2)
            )
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_Vector_wrong_option(self):
        try:
            self.SUT = HeightField('foo', Vector(1, 2, 3, 4))
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_non_existant_kw(self):
        try:
            self.SUT = HeightField('baz', foo='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_smooth_wrong_type(self):
        try:
            self.SUT = HeightField('baz', smooth='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_hierarchy_wrong_type(self):
        try:
            self.SUT = HeightField('baz', hierarchy='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_hf_type_wrong_type(self):
        try:
            self.SUT = HeightField('baz', hf_type=0.2)
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_hf_type_non_existant_value(self):
        try:
            self.SUT = HeightField('baz', hf_type='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_waterlevel_not_float(self):
        try:
            self.SUT = HeightField('baz', water_level='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
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
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_Vector_wrong_dimension(self):
        try:
            self.SUT = JuliaFractal(Vector(1, 2))
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_Vector_wrong_option(self):
        try:
            self.SUT = JuliaFractal(Vector(1, 2, 3, 4), Vector(1, 2, 3, 4))
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')

    def test_create_non_existant_kw(self):
        try:
            self.SUT = JuliaFractal(Vector(1, 2, 3, 4), foo='bar')
        except SdlSyntaxException:
            pass
        except Exception as e:
            self.fail('Unexpected exception thrown: %s \r\n %s' %
                      (type(e), traceback.format_exc()))
        else:
            self.fail('ExpectedException not thrown')
