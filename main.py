#!/usr/bin/python

import os
# import tempfile

from lgeo import lgeo_city

# infile = tempfile.NamedTemporaryFile(delete=False, suffix='.pov')
infile = open('main.pov', 'w')
infile.write(str(lgeo_city.main()))
infile.close()

os.system("povray +I" + infile.name + " +Omain.png +W800 +H600 +V +D +X +P")

# os.unlink(infile.name)
