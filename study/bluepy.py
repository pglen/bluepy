#!/usr/bin/env python

import os, sys, getopt, signal, select, string, time
import struct, stat, base64, random

#print(sys.version_info)

# Decorator for speed measure
def measure(func):
    def run(*args, **kwargs):
        ttt = time.time()
        ret = func(*args, **kwargs)
        print("Exe: %.3f us" % ((time.time() - ttt) * 1000000))
        return ret
    return run

if sys.version_info[0] < 3:
    import bluepy_c
else:
    from array import array
    import bluepy3 as bluepy_c

# Mirror 'c'  function versions

def version():
    return bluepy_c.version()

def builddate():
    return bluepy_c.builddate()

#@measure
def encrypt(buff, passwd):
    rrr = bluepy_c.encrypt(buff, passwd)
    return rrr

#@measure
def decrypt(buff, passwd):
    rrr = bluepy_c.decrypt(buff, passwd)
    return rrr

def tohex(buff):
    rrr = bluepy_c.tohex(buff);   #//buff.encode("cp437"))
    return rrr

def fromhex(buff):
    rrr = bluepy_c.fromhex(buff)
    return rrr

def destroy(buff, fill = 0):
    bluepy_c.destroy(buff, fill)
    pass

OPEN = bluepy_c.OPEN
author = bluepy_c.author
dict = bluepy_c.__dict__
#print("dict", dict)

# EOF
