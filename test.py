#!/usr/bin/python
# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Toennishoff, 2013.

Testing Scene
"""
import os

from lgeo import testscene

# INFILE = tempfile.NamedTemporaryFile(delete=False, suffix='.pov')
INFILE = open('test.pov', 'w')
INFILE.write(str(testscene.main()))
INFILE.close()

os.system("povray +I" + INFILE.name + " +Omain.png +W1280 +H960 +V +D +X +P")

# os.unlink(INFILE.name)
