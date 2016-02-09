# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Tönnishoff, 2013.

based on:
PyPov-0.0.X Copyright (c) Simon Burton, 2003
See LICENSE file.

Some modifications by W.T. Bridgman, 2006-2007.

"""

from logging import debug

from pov.tests.ObjectModifierTest import TranslateTestCase

from pov.tests.OtherTest import CameraTestCase
from pov.tests.OtherTest import LightSourceTestCase

from pov.tests.TextureTest import FinishTestCase
from pov.tests.TextureTest import ColorMapTestCase
from pov.tests.TextureTest import NormalTestCase
from pov.tests.TextureTest import PigmentTestCase
from pov.tests.TextureTest import TextureTestCase


debug('Loaded ' + TranslateTestCase.__name__)

debug('Loaded ' + CameraTestCase.__name__)
debug('Loaded ' + LightSourceTestCase.__name__)

debug('Loaded ' + FinishTestCase.__name__)
debug('Loaded ' + ColorMapTestCase.__name__)
debug('Loaded ' + NormalTestCase.__name__)
debug('Loaded ' + PigmentTestCase.__name__)
debug('Loaded ' + TextureTestCase.__name__)
