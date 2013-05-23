# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013
based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from __future__ import nested_scopes
import os
from logging import *
from Vector import Vector


class SceneItem(object):
    """
        Base class for POV objects.

        SCENE_ITEM:
            LANGUAGE_DIRECTIVES        |
            camera { CAMERA_ITEMS... } |
            OBJECTS                    |
            ATMOSPHERIC_EFFECTS        |
            global_settings { GLOBAL_ITEMS }
    """

    # All reserved identifiers for syntax checking purposes
    # @see: http://www.povray.org/documentation/view/3.6.1/226/
    __reserved_keywords = [
        'aa_level', 'aa_threshold', 'abs', 'absorption', 'accuracy', 'acos',
        'acosh', 'adaptive', 'adc_bailout', 'agate', 'agate_turb', 'all',
        'all_intersections', 'alpha', 'altitude', 'always_sample', 'ambient',
        'ambient_light', 'angle', 'aperture', 'append', 'arc_angle',
        'area_light', 'array', 'asc', 'ascii', 'asin', 'asinh', 'assumed_gamma',
        'atan', 'atan2', 'atanh', 'autostop', 'average',

        'b_spline', 'background', 'bezier_spline', 'bicubic_patch',
        'black_hole', 'blob', 'blue', 'blur_samples', 'bounded_by', 'box',
        'boxed', 'bozo', 'break', 'brick', 'brick_size', 'brightness',
        'brilliance', 'bump_map', 'bump_size', 'bumps',

        'camera', 'case', 'caustics', 'ceil', 'cells', 'charset', 'checker',
        'chr', 'circular', 'clipped_by', 'clock', 'clock_delta', 'clock_on',
        'collect', 'color', 'color_map', 'colour', 'colour_map', 'component',
        'composite', 'concat', 'cone', 'confidence', 'conic_sweep',
        'conserve_energy', 'contained_by', 'control0', 'control1', 'coords',
        'cos', 'cosh', 'count', 'crackle', 'crand', 'cube', 'cubic',
        'cubic_spline', 'cubic_wave', 'cutaway_textures', 'cylinder',
        'cylindrical',

        'debug', 'declare', 'default', 'defined', 'degrees', 'density',
        'density_file', 'density_map', 'dents', 'df3', 'difference', 'diffuse',
        'dimension_size', 'dimensions', 'direction', 'disc', 'dispersion',
        'dispersion_samples', 'dist_exp', 'distance', 'div', 'double_illuminate',

        'eccentricity', 'else', 'emission', 'end', 'error', 'error_bound',
        'evaluate', 'exp', 'expand_thresholds', 'exponent', 'exterior',
        'extinction',

        'face_indices', 'facets', 'fade_color', 'fade_colour', 'fade_distance',
        'fade_power', 'falloff', 'falloff_angle', 'false', 'fclose',
        'file_exists', 'filter', 'final_clock', 'final_frame', 'finish',
        'fisheye', 'flatness', 'flip', 'floor', 'focal_point', 'fog', 'fog_alt',
        'fog_offset', 'fog_type', 'fopen', 'form', 'frame_number', 'frequency',
        'fresnel', 'function',

        'gather', 'gif', 'global_lights', 'global_settings', 'gradient',
        'granite', 'gray', 'gray_threshold', 'green', 'height_field', 'hexagon',
        'hf_gray_16', 'hierarchy', 'hypercomplex', 'hollow', 'if', 'ifdef',
        'iff', 'ifndef', 'image_height', 'image_map', 'image_pattern',
        'image_width', 'include', 'initial_clock', 'initial_frame', 'inside',
        'inside_vector', 'int', 'interior', 'interior_texture', 'internal',
        'interpolate', 'intersection', 'intervals', 'inverse', 'ior', 'irid',
        'irid_wavelength', 'isosurface',

        'jitter'
'jpeg'
'julia'
'julia_fractal'

'lambda'
'lathe'
'leopard'
'light_group'
'light_source'
'linear_spline'
'linear_sweep'
'ln'
'load_file'
'local'
'location'
'log'
'look_at'
'looks_like'
'low_error_factor'

'macro'
'magnet'
'major_radius'
'mandel'
'map_type'
'marble'
'material'
'material_map'
'matrix'
'max'
'max_extent'
'max_gradient'
'max_intersections'
'max_iteration'
'max_sample'
'max_trace'
'max_trace_level'
'media'
'media_attenuation'
'media_interaction'
'merge'
'mesh'
'mesh2'
'metallic'
'method'
'metric'
'min'
'min_extent'
'minimum_reuse'
'mod'
'mortar'

natural_spline
nearest_count
no
no_bump_scale
no_image
no_reflection
no_shadow
noise_generator
normal
normal_indices
normal_map
normal_vectors
number_of_waves
o
object
octaves
off
offset
omega
omnimax
on
once
onion
open
orient
orientation
orthographic
p
panoramic
parallel
parametric
pass_through
pattern
perspective
pgm
phase
phong
phong_size
photons
pi
pigment
pigment_map
pigment_pattern
planar
plane
png
point_at
poly
poly_wave
polygon
pot
pow
ppm
precision
precompute
pretrace_end
pretrace_start
prism
prod
projected_through
pwr
q
quadratic_spline
quadric
quartic
quaternion
quick_color
quick_colour
quilted
r
radial
radians
radiosity
radius
rainbow
ramp_wave
rand
range
ratio
read
reciprocal
recursion_limit
red
reflection
reflection_exponent
refraction
render
repeat
rgb
rgbf
rgbft
rgbt
right
ripples
rotate
roughness
s
samples
save_file
scale
scallop_wave
scattering
seed
select
shadowless
sin
sine_wave
sinh
size
sky
sky_sphere
slice
slope
slope_map
smooth
smooth_triangle
solid
sor
spacing
specular
sphere
sphere_sweep
spherical
spiral1
spiral2
spline
split_union
spotlight
spotted
sqr
sqrt
statistics
str
strcmp
strength
strlen
strlwr
strupr
sturm
substr
sum
superellipsoid
switch
sys
t
t
tan
tanh
target
text
texture
texture_list
texture_map
tga
thickness
threshold
tiff
tightness
tile2
tiles
tolerance
toroidal
torus
trace
transform
translate
transmit
triangle
triangle_wave
true
ttf
turb_depth
turbulence
type
u
u
u_steps
ultra_wide_angle
undef
union
up
use_alpha
use_color
use_colour
use_index
utf8
uv_indices
uv_mapping
uv_vectors
v
v
v_steps
val
variance
vaxis_rotate
vcross
vdot
version
vertex_vectors
vlength
vnormalize
vrotate
vstr
vturbulence
w
warning
warp
water_level
waves
while
width
wood
wrinkles
write
x
x
y
y
yes
All reserved keywords
z
z
    ]
    def __init__(self, name, args=[], opts=[], kwargs=[]):
        """
            Base class for POV objects.

            @param name: POV object name
            @type name: string
            @param args: compulsory (comma separated?) pov args XX commas don't seem to matter?
            @type args: list
            @param opts: eg. CSG items
            @type opts: list
            @param kwargs: key value pairs
            @type kwargs: dict

            @TODO: move indentation check to own function
        """
        debug("%s: SceneItem.__init__(): Start: %s, %s, %s, %s" %
              (self.__class__.__name__, name, args, opts, kwargs))

        # format parameters
        self._format_args(args)
        self._format_opts(opts)
        self._format_kwargs(kwargs)

        #@todo: Does indentation really have to stay in the constructor??
        if not "indentation" in globals():
            global indentation
            indentation = 0
            debug("set initial indentation to 0")

        #Call syntax check methods
        self._check_arguments(args)
        self._check_opts(opts)
        self._check_kwargs(kwargs)

        self.name = name

        debug("%s: SceneItem.__init__(): Stop: %s, %s, %s, %s" %
              (self.__class__.__name__, name, args, opts, kwargs))

    #---------------------------------------------------------------------------
    # Pseudo private  methods
    #---------------------------------------------------------------------------

    def _indent(self):
        """
            Indent PoV code
        """
        global indentation
        indentation += 1
        debug("indent: %s", indentation)

    def _dedent(self):
        """
            Dedent PoV code
        """
        global indentation
        indentation -= 1
        debug("dedent: %s", indentation)
        if not indentation >= 0:
            raise IllegalStateException('Indentation below zero')

    def _getIndent(self):
        """
            Get indentation
        """
        global indentation
        return indentation

    def _block_begin(self):
        """
            Begin code block
                * return opening bracket and line separator
                * increase indentation
        """
        debug("begin block")
        code = " {" + os.linesep

        self._indent()

        return code

    def _block_end(self):
        """
            End code block
                * reduce indentation
                * add line with closing bracket
        """
        debug("end block: indentation= %s", indentation)

        if indentation == 0:
            # blank line if this is a top level end
            code = self._getLine()
        else:
            self._dedent()
            code = self._getLine("}")

        return code

    def _getLine(self, s=""):
        """
            format line of code with indentation and line separator
        """
        global indentation
        info("'" + "  " * indentation + s + "'")
        return "  " * indentation + s + os.linesep

    def _check_opts(self):
        '''
            Option Syntax checks

            to be overwritten in subclasses
        '''
        pass

    def _check_arguments(self):
        '''
            Argument Syntax checks

            to be overwritten in subclasses
        '''
        pass

    def _check_kwargs(self):
        '''
            Keyword Argument Syntax checks

            to be overwritten in subclasses
        '''
        pass

    def _format_args(self, args):
        '''
            format argument parameters
        '''
        args = list(args)
        for i in range(len(args)):
            args[i] = self.map_arg(args[i])
        self.args = self.flatten(args)

    def _format_opts(self, opts):
        '''
            format option parameters
        '''
        opts = list(opts)
        for i in range(len(opts)):
            opts[i] = self.map_arg(opts[i])
        self.opts = self.flatten(opts)

    def _format_kwargs(self, kwargs):
        '''
            format keyword parameters
        '''
        #debug('kwargs: %s', kwargs)
        self.kwargs = dict(kwargs)  # take a copy
        kwargs = dict(kwargs).items()
        #debug('kwargs: %s', kwargs)
        kwargs.reverse()
        #debug('kwargs: %s', kwargs)

        for key, val in kwargs:
            if type(val) == tuple or type(val) == list:
                self.kwargs[key] = self.map_arg(val)


    #---------------------------------------------------------------------------
    # Overloading magic methods
    #---------------------------------------------------------------------------

    def __str__(self):
        """
            return PoV code as string representation

            this method is meant to be overridden in subclasses
        """
        debug("SceneItem.__str__ %s, %s, %s", self.name, self.args, self.opts)

        return self.name

    def __setitem__(self, i, item):
        """
            Set Item magic method

            e.g. foo[i] = bar
        """
        if i < len(self.args):
            self.args[i] = self.map_arg(item)
        else:
            i -= len(self.args)
            if i < len(self.opts):
                self.opts[i] = self.map_arg(item)
            else:
                raise IndexError()

    def __getitem__(self, i):
        """
            Get Item magic method

            e.g. foo = bar[i]
        """
        if i < len(self.args):
            return self.args[i]
        else:
            i -= len(self.args)
            if i < len(self.opts):
                return self.opts[i]
            else:
                raise IndexError()

    def __eq__(self, other):
        '''
            Operator Overload "="
        '''
        if not isinstance(other, SceneItem):
            raise ArgumentError()
        a = self.name == other.name
        debug(str(self.name) + ' = ' + str(self.name))
        b = self.args == other.args
        debug(str(self.args) + ' = ' + str(self.args))
        c = self.opts == other.opts
        debug(str(self.opts) + ' = ' + str(self.opts))
        d = self.kwargs == other.kwargs
        debug(str(self.kwargs) + ' = ' + str(self.kwargs))
        return a & b & c & d

    #---------------------------------------------------------------------------
    # Public methods
    #---------------------------------------------------------------------------

    def append(self, *opts, **kwargs):
        """
            append Subitem(s) to Item

            works for Options and kwargs
        """

        # syntax check appended stuff
        self._check_opts(opts)
        self._check_kwargs(kwargs)

        for item in self.flatten(opts):
            self.opts.append(item)
        for key, val in kwargs.items():
            self.kwargs[key] = val

    def map_arg(self, arg):
        """
            Map an argument list to an appropriate format
        """
        if type(arg) in (tuple, list):
            # if multiple-component, floating-point value, return a vector
            if len(arg) and hasattr(arg[0], "__float__"):
                return Vector(arg)
        # else return the same format as the input value
        return arg

    def flatten(self, seq):
        '''
            flatten lists to one dimension
        '''
        seq = list(seq)
        i = 0
        while i < len(seq):
            if type(seq[i]) in (list, tuple):
                x = seq.pop(i)
                for item in x:
                    seq.insert(i, item)
                    i += 1
            else:
                i += 1
        return seq

