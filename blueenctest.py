#!/usr/bin/env python3

import sys, os

import bluepyenc

def mainfunct():
    #print( "Python Version:    ", "%d.%d.%d" % sys.version_info[:3])
    print( "Bluepoint Version: ", bluepyenc.version())
    print( "Builddate:         ",  bluepyenc.builddate())
    #print()
    buff = "Hello, this is a test string.";
    passw = "1234"

    if  len(sys.argv) > 1:
        buff = sys.argv[1]
    if  len(sys.argv) > 2:
        passw = sys.argv[2]

    print( "org:", "'" + buff + "'")
    enc = bluepyenc.encrypt( buff, passw)

    #print("enz: '" + dumpx(enc) + "'")
    hexenc = bluepyenc.tohex(enc)
    print("enc:", "'" +  hexenc + "'")

    '''uex = bluepyenc.fromhex(hexenc)
    print("enc: '" + dumpx(uex) + "'")'''

    dec = bluepyenc.decrypt(enc, passw)
    if sys.version_info[0] >= 3:
        dec = dec.decode("cp437")
    print("dec:", "'" + dec + "'")
    #de2 = bluepy.decrypt(enc, passw)
    #print("de2:", "'" + dec + "'")

    #hexx = bluepy.tohex(buff)
    #print( "hex:   ", hexx)
    #print( "unhex:",  "'" +  uex +"'")

    bluepyenc.destroy(enc)
    #print( "edd:", "'" + bluepy.tohex(enc) + "'")

    err = 0
    if dec != buff:
        print( "Test FAILED", file=sys.stderr)
        err = 1

    sys.exit(err)

if __name__ == '__main__':
    mainfunct()

# EOF
