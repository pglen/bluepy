#!/usr/bin/env python3

import sys, os

import bluepy3

def mainfunct():
    #print( "Python Version:    ", "%d.%d.%d" % sys.version_info[:3])
    print( "Bluepoint Version: ", bluepy3.version())
    print( "Builddate:         ",  bluepy3.builddate())
    #print()
    buff = "Hello, this is a test string.";
    passw = "1234"

    if  len(sys.argv) > 1:
        buff = sys.argv[1]
    if  len(sys.argv) > 2:
        passw = sys.argv[2]

    print( "org:", "'" + buff + "'")
    enc = bluepy3.encrypt( buff, passw)

    #print("enz: '" + dumpx(enc) + "'")
    hexenc = bluepy3.tohex(enc)
    print("enc:", "'" +  hexenc + "'")

    '''uex = bluepy3.fromhex(hexenc)
    print("enc: '" + dumpx(uex) + "'")'''

    dec = bluepy3.decrypt(enc, passw)
    if sys.version_info[0] >= 3:
        dec = dec.decode("cp437")
    print("dec:", "'" + dec + "'")
    #de2 = bluepy.decrypt(enc, passw)
    #print("de2:", "'" + dec + "'")

    #hexx = bluepy.tohex(buff)
    #print( "hex:   ", hexx)
    #print( "unhex:",  "'" +  uex +"'")

    bluepy3.destroy(enc)
    #print( "edd:", "'" + bluepy.tohex(enc) + "'")

    err = 0
    if dec != buff:
        print( "Test FAILED", file=sys.stderr)
        err = 1

    sys.exit(err)

if __name__ == '__main__':
    mainfunct()

# EOF
