#!/usr/bin/env python2

import os, sys

from distutils.core import Extension, setup

#os.putenv("APPLY_LP2002043_UBUNTU_CFLAGS_WORKAROUND", "1")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.argv = [sys.argv[0], 'build_ext', '-i']
setup(ext_modules = [Extension('bluepy2', ["bluepy_c.c", "bluepoint2.c"])])


