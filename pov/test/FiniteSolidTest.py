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
from pov.finite_solid.Sphere import Sphere
from pov.finite_solid.Lathe import Lathe


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
        with self.assertRaisesRegexp(SdlSyntaxException, 'Parameter v1 not of type Vector'):
            self.SUT = Box(
                'foo',
                Vector(5, 6, 7),
                ObjectModifier('foo')
            )

    def test_create_v2_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Parameter v2 not of type Vector'):
            self.SUT = Box(
                Vector(5, 6, 7),
                'foo',
                ObjectModifier('foo')
            )

    def test_create_v1_wrong_length(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Vector v1 has more or less than 3 dimensions'):
            self.SUT = Box(
                Vector(1, 2),
                Vector(5, 6, 7),
                ObjectModifier('foo')
            )

    def test_create_v2_wrong_length(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Vector v2 has more or less than 3 dimensions'):
            self.SUT = Box(
                Vector(1, 2, 3),
                Vector(4, 5, 6, 7),
                ObjectModifier('foo')
            )

    def test_create_option_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Only ObjectModifier objects may be passed as options'):
            self.SUT = Box(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                Vector(1, 2)
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
        with self.assertRaisesRegexp(SdlSyntaxException, 'Invalid keyword: foo'):
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                foo=True
            )

    def test_create_open_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of keyword open is not boolean'):
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_baseradius_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Param base radius is not of type int or float'):
            self.SUT = Cone(
                Vector(1, 2, 3),
                'foo',
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_capradius_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Param cap radius is not of type int or float'):
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                'foo',
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_option_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Only ObjectModifier objects may be passed as options'):
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                Vector(1, 2),
                open=0.3
            )

    def test_create_basepoint_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Parameter basepoint is not of type Vector'):
            self.SUT = Cone(
                'foo',
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_cappoint_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Parameter cappoint is not of type Vector'):
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                'foo',
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_basepoint_wrong_length(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Base point Vector has more or less than 3 dimensions'):
            self.SUT = Cone(
                Vector(1, 2, 3, 9),
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_cappoint_wrong_length(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Cap point Vector has more or less than 3 dimensions'):
            self.SUT = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7, 9),
                8,
                ObjectModifier('foo'),
                open=0.3
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
        with self.assertRaisesRegexp(SdlSyntaxException, 'Invalid keyword: bar'):
            self.SUT = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                bar=True
            )

    def test_create_open_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of keyword open is not boolean'):
            self.SUT = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open='foo'
            )

    def test_create_basepoint_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Parameter basepoint is not of type Vector'):
            self.SUT = Cylinder(
                'foo',
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_cappoint_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Parameter cappoint is not of type Vector'):
            self.SUT = Cylinder(
                Vector(1, 2, 3),
                'foo',
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_basepoint_wrong_length(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Base point Vector has more or less than 3 dimensions'):
            self.SUT = Cylinder(
                Vector(1, 2, 3, 9),
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_cappoint_wrong_length(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Cap point Vector has more or less than 3 dimensions'):
            self.SUT = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7, 9),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_radius_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Param radius is not of type int or float'):
            self.SUT = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                'foo',
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_ObjectModifier_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Only ObjectModifier objects may be passed as options'):
            self.SUT = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                8,
                'foo',
                open=0.3
            )


class HeightFieldTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = HeightField('fixture/test.gif')

    def test_creation(self):
        self.assertIsInstance(self.SUT, HeightField)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_create_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of Argument 0 is expectet to be type str but got float'):
            self.SUT = HeightField(1.0)

    def test_create_Vector_wrong_option(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Invalid option type Vector not in allowed opts \n\\[\'ObjectModifier\']'):
            self.SUT = HeightField('fixture/test.gif', Vector(1, 2, 3, 4))

    def test_create_non_existant_kw(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'No such Keyword: foo'):
            self.SUT = HeightField('fixture/test.gif', foo='bar')

    def test_create_smooth_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of KW Argument smooth is expectet to be type bool but got str'):
            self.SUT = HeightField('fixture/test.gif', smooth='bar')

    def test_create_hierarchy_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of KW Argument hierarchy is expectet to be type bool but got str'):
            self.SUT = HeightField('fixture/test.gif', hierarchy='bar')

    def test_create_hf_type_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of KW Argument hf_type is expectet to be type str but got float'):
            self.SUT = HeightField('fixture/test.gif', hf_type=0.2)

    def test_create_hf_type_non_existant_value(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of KW Argument hf_type is expectet to be in \\[\'gif\', \'tga\', \'pot\', \'png\', \'pgm\', \'ppm\', \'jpeg\', \'tiff\', \'sys\', \'function\'] but got bar'):
            self.SUT = HeightField('fixture/test.gif', hf_type='bar')

    def test_create_hf_non_existant_file(self):
        with self.assertRaisesRegexp(IOError, 'No such file: %s%s%s' % (os.getcwd(), os.sep, 'fixture/nonexistant.gif')):
            self.SUT = HeightField('fixture/nonexistant.gif', hf_type='bar')

    def test_create_waterlevel_not_float(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of KW Argument water_level is expectet to be type float but got str'):
            self.SUT = HeightField('fixture/test.gif', water_level='bar')

    def test_toString(self):
        le = os.linesep

        second = 'height_field {' + le
        second += '  "fixture/test.gif"' + le
        second += '}' + le

        self.assertEqual(str(self.SUT), second)


class JuliaFractalTestCase(unittest.TestCase):
    def setUp(self):
        self.SUT = JuliaFractal(Vector(1, 2, 3, 4))

    def test_creation(self):
        self.assertIsInstance(self.SUT, JuliaFractal)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_create_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of Argument 0 is expectet to be type Vector but got str'):
            self.SUT = JuliaFractal('foo')

    def test_create_Vector_wrong_dimension(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Vector param4d has more or less than 4 dimensions'):
            self.SUT = JuliaFractal(Vector(1, 2))

    def test_create_Vector_wrong_option(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Invalid option type Vector not in allowed opts \n\\[\\\'ObjectModifier\\\']'):
            self.SUT = JuliaFractal(Vector(1, 2, 3, 4), Vector(1, 2, 3, 4))

    def test_create_non_existant_kw(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'No such Keyword: foo'):
            self.SUT = JuliaFractal(Vector(1, 2, 3, 4), foo='bar')

    def test_toString(self):
        le = os.linesep

        second = 'julia_fractal {' + le
        second += '  <1, 2, 3, 4>' + le
        second += '}' + le

        self.assertEqual(str(self.SUT), second)


class SphereTestCase(unittest.TestCase):
    '''
        SPHERE:
            sphere
            {
                <Center>, Radius
                [OBJECT_MODIFIERS...]
            }
    '''
    def setUp(self):
        self.SUT = Sphere(
            Vector(1, 2, 3),
            8
        )

    def test_creation(self):
        self.assertIsInstance(self.SUT, Sphere)
        self.assertIsInstance(self.SUT, SceneItem)

        le = os.linesep
        second = 'sphere {' + le
        second += '  <1, 2, 3>, 8' + le
        second += '}' + le

        self.assertEqual(
            str(self.SUT),
            second
        )

    def test_creationWithOption(self):
        self.SUT = Sphere(
            Vector(1, 2, 3),
            8,
            ObjectModifier('foo')
        )

        self.assertIsInstance(self.SUT, Sphere)
        self.assertIsInstance(self.SUT, SceneItem)

    def test_create_non_existant_kw(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'No such Keyword: bar'):
            self.SUT = Sphere(
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                bar=True
            )

    def test_create_center_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of Argument 0 is expectet to be type Vector but got str'):
            self.SUT = Sphere(
                'foo',
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_center_wrong_length(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Center point Vector has more or less than 3 dimensions'):
            self.SUT = Sphere(
                Vector(1, 2, 3, 9),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_radius_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of Argument 1 is expectet to be type \\(\'float\', \'int\'\\) but got str'):
            self.SUT = Sphere(
                Vector(1, 2, 3),
                'foo',
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_ObjectModifier_wrong_type(self):
        with self.assertRaisesRegexp(SdlSyntaxException, 'Invalid option type str not in allowed opts \n\\[\\\'ObjectModifier\\\']'):
            self.SUT = Sphere(
                Vector(1, 2, 3),
                8,
                'foo',
                open=0.3
            )


class LatheTestCase(unittest.TestCase):
    '''
        LATHE:
            lathe
            {
                [SPLINE_TYPE] Number_Of_Points, <Point_1>
                <Point_2>... <Point_n>
                [LATHE_MODIFIER...]
            }
        SPLINE_TYPE:
            linear_spline | quadratic_spline | cubic_spline | bezier_spline
        LATHE_MODIFIER:
            sturm | OBJECT_MODIFIER
    '''

    def setUp(self):
        self.SUT = Lathe('linear_spline', 1, [Vector(1, 2, 3)])

    def test_creation(self):
        self.assertIsInstance(self.SUT, Lathe)
        self.assertIsInstance(self.SUT, SceneItem)

#    def test_create_wrong_type(self):
#        with self.assertRaisesRegexp(SdlSyntaxException, 'Value of Argument 0 is expectet to be type str but got float'):
#            self.SUT = HeightField(1.0)

    def test_toString(self):
        le = os.linesep

        second = 'lathe {' + le
        second += '  linear_spline, 1, <1, 2, 3>' + le
        second += '}' + le

        self.assertEqual(str(self.SUT), second)


