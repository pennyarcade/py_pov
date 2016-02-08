#!/usr/bin/python
# coding=UTF-8
u"""
Py_Pov 0.0.1 Copyright (c) Martin Toennishoff, 2013.

Testing Scene
"""
import os

from lgeo import lgeo_city

# INFILE = tempfile.NamedTemporaryFile(delete=False, suffix='.pov')
INFILE = open('main.pov', 'w')
INFILE.write(str(lgeo_city.main()))
INFILE.close()

os.system("povray +I" + INFILE.name + " +Omain.png +W800 +H600 +V +D +X +P")

# os.unlink(INFILE.name)
