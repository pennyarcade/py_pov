#!/usr/bin/python

import os
import tempfile

from lgeo import lgeo_city

#f = tempfile.NamedTemporaryFile(delete=False, suffix='.pov')
f = open('main.pov', 'w')
f.write(str(lgeo_city.main()))
f.close()

os.system("povray +I" + f.name + " +Omain.png +W800 +H600 +V +D +X +P")

#os.unlink(f.name)
