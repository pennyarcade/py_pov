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
# import traceback

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
    """
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
    """

    def setUp(self):
        """
            Set up fixture
        """
        self.sut = Blob()

    def test_create(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, Blob)
        self.assertIsInstance(self.sut, SceneItem)

        second = 'blob {' + os.linesep + '}' + os.linesep

        self.assertEqual(str(self.sut), second)


class BoxTestCase(unittest.TestCase):
    """
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
            rotate VECTOR | scale VECTOR | translate VECTOR
                | TRANSFORM | MATRIX
        TRANSFORM:
            transform TRANSFORM_IDENTIFIER
                | transform { [TRANSFORM_ITEM...] }

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
            @ToDo: KwArg: 0..1 transform string; existing identifier;
                   transform object
            @ToDo: only one "transform"
    """

    def setUp(self):
        """
            Set up fixture
        """
        self.sut = Box(Vector(1, 2, 3), Vector(4, 5, 6))

    def test_create(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, Box)
        self.assertIsInstance(self.sut, SceneItem)

        second = 'box {' + os.linesep
        second += '  <1, 2, 3>, <4, 5, 6>' + os.linesep
        second += '}' + os.linesep

        self.assertEqual(
            str(self.sut),
            second
        )

    def test_create_with_option(self):
        """
            @Todo: DocString
        """
        sut = Box(Vector(1, 2, 3), Vector(4, 5, 6), ObjectModifier('foo'))

        self.assertIsInstance(sut, Box)
        self.assertIsInstance(sut, SceneItem)

    def test_create_v1_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter v1 not of type Vector'
        ):
            self.sut = Box(
                'foo',
                Vector(5, 6, 7),
                ObjectModifier('foo')
            )

    def test_create_v2_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter v2 not of type Vector'
        ):
            self.sut = Box(
                Vector(5, 6, 7),
                'foo',
                ObjectModifier('foo')
            )

    def test_create_v1_wrong_length(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Vector v1 has more or less than 3 dimensions'
        ):
            self.sut = Box(
                Vector(1, 2),
                Vector(5, 6, 7),
                ObjectModifier('foo')
            )

    def test_create_v2_wrong_length(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Vector v2 has more or less than 3 dimensions'
        ):
            self.sut = Box(
                Vector(1, 2, 3),
                Vector(4, 5, 6, 7),
                ObjectModifier('foo')
            )

    def test_create_option_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Only ObjectModifier objects may be passed as options'
        ):
            self.sut = Box(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                Vector(1, 2)
            )


class ConeTestCase(unittest.TestCase):
    """
        Test Cone class
    """
    def setUp(self):
        """
            Set up fixture
        """
        self.sut = Cone(
            Vector(1, 2, 3),
            4,
            Vector(5, 6, 7),
            8
        )

    def test_creation(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, Cone)
        self.assertIsInstance(self.sut, SceneItem)

        lsp = os.linesep
        second = 'cone {' + lsp
        second += '  <1, 2, 3>, 4, <5, 6, 7>, 8' + lsp
        second += '}' + lsp

        self.assertEqual(
            str(self.sut),
            second
        )

    def test_creation_with_option_and_kwarg(self):
        """
            Test parameter syntax
        """
        self.sut = Cone(
            Vector(1, 2, 3),
            4,
            Vector(5, 6, 7),
            8,
            ObjectModifier('foo'),
            open=True
        )

        self.assertIsInstance(self.sut, Cone)
        self.assertIsInstance(self.sut, SceneItem)

    def test_create_non_existant_kw(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Invalid keyword: foo'
        ):
            self.sut = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                foo=True
            )

    def test_create_open_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Value of keyword open is not boolean'
        ):
            self.sut = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_baseradius_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Param base radius is not of type int or float'
        ):
            self.sut = Cone(
                Vector(1, 2, 3),
                'foo',
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_capradius_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Param cap radius is not of type int or float'
        ):
            self.sut = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                'foo',
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_option_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Only ObjectModifier objects may be passed as options'
        ):
            self.sut = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7),
                8,
                Vector(1, 2),
                open=0.3
            )

    def test_create_basepoint_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter basepoint is not of type Vector'
        ):
            self.sut = Cone(
                'foo',
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_cappoint_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter cappoint is not of type Vector'
        ):
            self.sut = Cone(
                Vector(1, 2, 3),
                4,
                'foo',
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_basepoint_wrong_length(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Base point Vector has more or less than 3 dimensions'
        ):
            self.sut = Cone(
                Vector(1, 2, 3, 9),
                4,
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_cappoint_wrong_length(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Cap point Vector has more or less than 3 dimensions'
        ):
            self.sut = Cone(
                Vector(1, 2, 3),
                4,
                Vector(5, 6, 7, 9),
                8,
                ObjectModifier('foo'),
                open=0.3
            )


class CylinderTestCase(unittest.TestCase):
    """
        Test Cylinder class
    """
    def setUp(self):
        """
            Set up fixture
        """
        self.sut = Cylinder(
            Vector(1, 2, 3),
            Vector(5, 6, 7),
            8
        )

    def test_creation(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, Cylinder)
        self.assertIsInstance(self.sut, SceneItem)

        second = 'cylinder {' + os.linesep
        second += '  <1, 2, 3>, <5, 6, 7>, 8' + os.linesep
        second += '}' + os.linesep

        self.assertEqual(
            str(self.sut),
            second
        )

    def test_creation_with_option_and_kwarg(self):
        """
            Test parameter syntax
        """
        self.sut = Cylinder(
            Vector(1, 2, 3),
            Vector(5, 6, 7),
            8,
            ObjectModifier('foo'),
            open=True
        )

        self.assertIsInstance(self.sut, Cylinder)
        self.assertIsInstance(self.sut, SceneItem)

    def test_create_non_existant_kw(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Invalid keyword: bar'
        ):
            self.sut = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                bar=True
            )

    def test_create_open_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Value of keyword open is not boolean'
        ):
            self.sut = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open='foo'
            )

    def test_create_basepoint_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter basepoint is not of type Vector'
        ):
            self.sut = Cylinder(
                'foo',
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_cappoint_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'Parameter cappoint is not of type Vector'
        ):
            self.sut = Cylinder(
                Vector(1, 2, 3),
                'foo',
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_basepoint_wrong_length(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Base point Vector has more or less than 3 dimensions'
        ):
            self.sut = Cylinder(
                Vector(1, 2, 3, 9),
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_cappoint_wrong_length(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Cap point Vector has more or less than 3 dimensions'
        ):
            self.sut = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7, 9),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_radius_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Param radius is not of type int or float'
        ):
            self.sut = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                'foo',
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_object_modifier_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Only ObjectModifier objects may be passed as options'
        ):
            self.sut = Cylinder(
                Vector(1, 2, 3),
                Vector(5, 6, 7),
                8,
                'foo',
                open=0.3
            )


class HeightFieldTestCase(unittest.TestCase):
    """
        Test HeightField class
    """
    def setUp(self):
        """
            Set up fixture
        """
        self.sut = HeightField('pov/tests/fixture/test.gif')

    def test_creation(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, HeightField)
        self.assertIsInstance(self.sut, SceneItem)

    def test_create_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Value of Argument 0 is expectet to be type str but got float'
        ):
            self.sut = HeightField(1.0)

    def test_create_vector_wrong_option(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            r'Invalid option type Vector not in allowed opts\[.*]'
        ):
            self.sut = HeightField('pov/tests/fixture/test.gif', Vector(1, 2, 3, 4))

    def test_create_non_existant_kw(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'No such Keyword: foo'
        ):
            self.sut = HeightField('pov/tests/fixture/test.gif', foo='bar')

    def test_create_smooth_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            ' '.join((
                'Value of KW Argument smooth is',
                'expectet to be type bool but got str'
            ))
        ):
            self.sut = HeightField('pov/tests/fixture/test.gif', smooth='bar')

    def test_create_hierarchy_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            ' '.join((
                'Value of KW Argument hierarchy is expectet',
                'to be type bool but got str'
            ))
        ):
            self.sut = HeightField('pov/tests/fixture/test.gif', hierarchy='bar')

    def test_create_hf_type_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            ' '.join((
                'Value of KW Argument hf_type is expectet',
                'to be type str but got float'
            ))
        ):
            self.sut = HeightField('pov/tests/fixture/test.gif', hf_type=0.2)

    def test_create_hf_type_non_existant_value(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            ' '.join((
                'Value of KW Argument hf_type is expectet to be in',
                '\\[\'gif\', \'tga\', \'pot\', \'png\', \'pgm\', \'ppm\',',
                '\'jpeg\', \'tiff\', \'sys\', \'function\'] but got bar'
            ))
        ):
            self.sut = HeightField('pov/tests/fixture/test.gif', hf_type='bar')

    def test_create_hf_non_existant_file(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            IOError,
            'No such file: %s%s%s' % (
                os.getcwd(), os.sep, 'fixture/nonexistant.gif'
            )
        ):
            self.sut = HeightField('fixture/nonexistant.gif', hf_type='bar')

    def test_create_waterlevel_not_float(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            ' '.join((
                'Value of KW Argument water_level is',
                'expectet to be type float but got str'
            ))
        ):
            self.sut = HeightField('pov/tests/fixture/test.gif', water_level='bar')

    def test_to_string(self):
        """
            Test sut.__str__()
        """
        second = 'height_field {' + os.linesep
        second += '  "pov/tests/fixture/test.gif"' + os.linesep
        second += '}' + os.linesep

        self.assertEqual(str(self.sut), second)


class JuliaFractalTestCase(unittest.TestCase):
    """
        Test JuliaFractal class
    """
    def setUp(self):
        """
            Set up fixture
        """
        self.sut = JuliaFractal(Vector(1, 2, 3, 4))

    def test_creation(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, JuliaFractal)
        self.assertIsInstance(self.sut, SceneItem)

    def test_create_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Value of Argument 0 is expectet to be type Vector but got str'
        ):
            self.sut = JuliaFractal('foo')

    def test_create_vector_wrong_dimension(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Vector param4d has more or less than 4 dimensions'
        ):
            self.sut = JuliaFractal(Vector(1, 2))

    def test_create_vector_wrong_option(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            r"Invalid option type Vector not in allowed opts\[.*]"
        ):
            self.sut = JuliaFractal(Vector(1, 2, 3, 4), Vector(1, 2, 3, 4))

    def test_create_non_existant_kw(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'No such Keyword: foo'
        ):
            self.sut = JuliaFractal(Vector(1, 2, 3, 4), foo='bar')

    def test_to_string(self):
        """
            Test sut.__str__()
        """
        second = 'julia_fractal {' + os.linesep
        second += '  <1, 2, 3, 4>' + os.linesep
        second += '}' + os.linesep

        self.assertEqual(str(self.sut), second)


class SphereTestCase(unittest.TestCase):
    """
        SPHERE:
            sphere
            {
                <Center>, Radius
                [OBJECT_MODIFIERS...]
            }
    """

    def setUp(self):
        """
            Set up fixture
        """
        self.sut = Sphere(
            Vector(1, 2, 3),
            8
        )

    def test_creation(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, Sphere)
        self.assertIsInstance(self.sut, SceneItem)

        lsp = os.linesep
        second = 'sphere {' + lsp
        second += '  <1, 2, 3>, 8' + lsp
        second += '}' + lsp

        self.assertEqual(
            str(self.sut),
            second
        )

    def test_creation_with_option(self):
        """
            Test parameter syntax
        """
        self.sut = Sphere(
            Vector(1, 2, 3),
            8,
            ObjectModifier('foo')
        )

        self.assertIsInstance(self.sut, Sphere)
        self.assertIsInstance(self.sut, SceneItem)

    def test_create_non_existant_kw(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException, 'No such Keyword: bar'
        ):
            self.sut = Sphere(
                Vector(5, 6, 7),
                8,
                ObjectModifier('foo'),
                bar=True
            )

    def test_create_center_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Value of Argument 0 is expectet to be type Vector but got str'
        ):
            self.sut = Sphere(
                'foo',
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_center_wrong_length(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            'Center point Vector has more or less than 3 dimensions'
        ):
            self.sut = Sphere(
                Vector(1, 2, 3, 9),
                8,
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_radius_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            ' '.join((
                'Value of Argument 1 is expectet to be type',
                '\\(\'float\', \'int\'\\) but got str'
            ))
        ):
            self.sut = Sphere(
                Vector(1, 2, 3),
                'foo',
                ObjectModifier('foo'),
                open=0.3
            )

    def test_create_object_modifier_wrong_type(self):
        """
            Test parameter syntax
        """
        with self.assertRaisesRegexp(
            SdlSyntaxException,
            r'Invalid option type str not in allowed opts\[.*]'
        ):
            self.sut = Sphere(
                Vector(1, 2, 3),
                8,
                'foo',
                open=0.3
            )


class LatheTestCase(unittest.TestCase):
    """
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
    """

    def setUp(self):
        """
            Set up fixture
        """
        self.sut = Lathe(
            'linear_spline', 2, [Vector(1, 2, 3), Vector(1, 2, 3)]
        )

    def test_creation(self):
        """
            Test creation and inheritance
        """
        self.assertIsInstance(self.sut, Lathe)
        self.assertIsInstance(self.sut, SceneItem)

#    def test_create_wrong_type(self):
#        with self.assertRaisesRegexp(
#            SdlSyntaxException,
#            'Value of Argument 0 is expectet to be type str but got float'
#        ):
#            self.sut = HeightField(1.0)

    def test_to_string(self):
        """
            Test sut.__str__()
        """
        second = 'lathe {' + os.linesep
        second += '  linear_spline, 2, <1, 2, 3>, <1, 2, 3>' + os.linesep
        second += '}' + os.linesep

        self.assertEqual(str(self.sut), second)
