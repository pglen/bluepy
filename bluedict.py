#!/usr/bin/env python

from __future__ import print_function

import sys, os

sys.path.insert(0, os.path.abspath('./'))

import bluepy3

if __name__ == '__main__':

    #print(bluepy3.__dict__)

    print( "Version:   ", bluepy3.version())
    print( "Builddate: ",  bluepy3.builddate())

    print( "Const:     ", bluepy3.OPEN)
    print( "Const:     ", bluepy3.author)

    #print( bluepy3.dict)
    #for aa in bluepy3.dict.keys():
        #print( aa )
        #print( bluepy3.dict[aa].__doc__)
        #print( )

# EOF
