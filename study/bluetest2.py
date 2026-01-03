#!/usr/bin/env python3

from __future__ import print_function

import sys, os

import bluepy2

def mainfunct():
    #print( "Python Version:    ", "%d.%d.%d" % sys.version_info[:3])
    print( "Bluepoint Version: ", bluepy2.version())
    print( "Builddate:         ",  bluepy2.builddate())
    #print()
    buff = "Hello, this is a test string.";
    passw = "1234"

    if  len(sys.argv) > 1:
        buff = sys.argv[1]
    if  len(sys.argv) > 2:
        passw = sys.argv[2]

    print( "org:", "'" + buff + "'")
    enc = bluepy2.encrypt( buff, passw)

    #print("enz: '" + dumpx(enc) + "'")
    hexenc = bluepy2.tohex(enc)
    print("enc:", "'" +  hexenc + "'")

    '''uex = bluepy2.fromhex(hexenc)
    print("enc: '" + dumpx(uex) + "'")'''

    dec = bluepy2.decrypt(enc, passw)
    if sys.version_info[0] >= 3:
        dec = dec.decode("cp437")
    print("dec:", "'" + dec + "'")
    #de2 = bluepy.decrypt(enc, passw)
    #print("de2:", "'" + dec + "'")

    #hexx = bluepy.tohex(buff)
    #print( "hex:   ", hexx)
    #print( "unhex:",  "'" +  uex +"'")

    bluepy2.destroy(enc)
    #print( "edd:", "'" + bluepy.tohex(enc) + "'")

    err = 0
    if dec != buff:
        print( "Test FAILED")
        err = 1

    sys.exit(err)

if __name__ == '__main__':
    mainfunct()

# EOF
