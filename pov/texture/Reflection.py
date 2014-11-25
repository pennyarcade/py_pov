# coding=UTF-8
"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""


from pov.basic.BlockObject import BlockObject


class Reflection(BlockObject):
    '''
        FINISH:
            Jump to SDL
            finish { [FINISH_IDENTIFIER] [FINISH_ITEMS] }
        FINISH_ITEMS:
            [ambient COLOR] & [diffuse FLOAT] & [brilliance FLOAT]
                & [PHONG] & [SPECULAR] & [REFLECTION] & [IRID]
                & [crand FLOAT] & [conserve_energy [BOOL]]
        PHONG:
            phong FLOAT & [phong_size FLOAT] & [metallic [FLOAT]]
        SPECULAR:
            specular FLOAT & [roughness FLOAT] & [metallic [FLOAT]]
        REFLECTION:
            reflection COLOR [reflection_exponent FLOAT] |
            reflection { [COLOR,] COLOR [REFLECTION_ITEMS] }
        REFLECTION_ITEMS:
            [fresnel BOOL] & [falloff FLOAT] & [exponent FLOAT]
                & [metallic [FLOAT]]
            Must also use interior {ior FLOAT} in the object
                when fresnel is used.
        IRID:
            irid { F_AMOUNT [IRID_ITEMS] }
        IRID_ITEMS:
            [thickness FLOAT] & [turbulence FLOAT]
    '''

    def __init__(self, *opts, **kwargs):
        '''
            Create Reflection object

            @todo: implement
            @todo: Syntax checks
        '''
        super(Reflection, self).__init__('reflection', [], opts, kwargs)

        if 'metallic' in self.kwargs and self.kwargs['metallic'] is True:
            del self.kwargs['metallic']
            self.args.append('metallic')
