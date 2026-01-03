# Python Bluepoint Encryption
## Full symetric block cypher encryption algorythm

### Quick example:

        import bluepyenc
        buff = "Hello, this is a test string.";
        passw = "1234"                          # This is a test
        enc = bluepyenc.encrypt(buff, passw)
        dec = bluepyenc.decrypt(enc, passw)
        assert buff == dec

  The power of the encryption comes from the following primitives:
(implemented as 'C' macros)

        HECTOR(op)              use op with vector highs
        PASSLOOP(op)            use op with pass as vector
        FWLOOP(op)              forward loop traverse
        FWLOOP2(op)             forward loop variation
        BWLOOP(op)              backward loop
        BWLOOP2(op)             backward loop variation
        MIXIT(op)               mix op on first part with second part
        MIXITR(op)              mix op on first part with second part reverse
        MIXIT2(op)              mix op on first part with second part variation
        MIXIT2R(op)             mix op on first part with second part variation in reverse
        MIXIT4(op)              mix quarter length

 These are then added into encrypt operations. Please note that the parameter op
is a mathematical / logical operation. (plus, minus, xor ...)
 The decryption is done in reverse order and reverse operator. (ex: '+' -> '-')

  The power comes from the arbitrary order of operators and the arbitrary injection
of reversible mathematical / logical operators.

## Bluepy has the following operator stack:

Encryption:

    PASSLOOP(+)
    MIXIT2(+)   MIXIT2R(+)
    HECTOR(+)   FWLOOP(+)
    MIXIT2(+)   MIXIT2R(+)
    PASSLOOP(+) FWLOOP(+)
    HECTOR(+)   FWLOOP(+)
    MIXITR(+)
    BWLOOP(+)   HECTOR(+)

Decryption:

    HECTOR(-)   BWLOOP2(-)
    MIXITR(-)
    FWLOOP2(-)  HECTOR(-)
    FWLOOP2(-)  PASSLOOP(-)
    MIXIT2R(-)  MIXIT2(-)
    FWLOOP2(-)  HECTOR(-)
    MIXIT2R(-)  MIXIT2(-)
    PASSLOOP(-)

 The resulting bit propagation is such high quality, that a single bit change
in the original text will change every byte in the resulting block.
(see bit description study in the code's directory)

 One may create a custom encryption by altering the operator stack in the 'C'
source.

 This beats current industrial strength encryptions, and perhaps qualifies for the
quantum challenge.

 Decryption is done by applying the ops in reverse, both by order and meaning.
This is very apparent in the functions ENCRYPT() and DECRYPT().  (see source)

## Encryption quality test:

 The cyphertext is tested for randomness with the 'dieharder' suite. All tests
are passed. Below, is an extract of the utility's printout.

       diehard_birthdays|   0|       100|     100|0.07973936|  PASSED
          diehard_operm5|   0|   1000000|     100|0.22646819|  PASSED
      diehard_rank_32x32|   0|     40000|     100|0.62699248|  PASSED
        diehard_rank_6x8|   0|    100000|     100|0.66828243|  PASSED
       diehard_bitstream|   0|   2097152|     100|0.55151892|  PASSED
            diehard_opso|   0|   2097152|     100|0.04670626|  PASSED
            diehard_oqso|   0|   2097152|     100|0.06864521|  PASSED
             diehard_dna|   0|   2097152|     100|0.72141254|  PASSED
    diehard_count_1s_str|   0|    256000|     100|0.68376408|  PASSED

## The bluefile encryption / decryption utility

This utility can be used as a quick command line encryption / decryption utility.
One of encrypt / decrypt must be specified.

        Usage: blueencfile.py [-e] [-d] [options] fromfile tofile
        Specify -e for encrypt -d decrypt
        Options:    -p pass   - pass to use
                    -f        - force overwrite
                    -v        - Verbose
                    -V        - Print version
                    -q        - Quiet
                    -h        - Help
TODO;

 Started the virtual machine operation, where the encryption is run through
a virtual machine stack, following a pre-made recipe or getting hints from the
password.

## History:

    Release                 Thu 13.Oct.2022
    Pip install             Sat 03.Jan.2026
    Published on GH         Sun 04.Jan.2026

Warning!

  No meta data is stored. It is left up to the caller to maintain integrity
beyond the cyphertext operations.

 The encryption / decryption has to run with the same vector, same pass same
block length. Make sure you know what you are doing, as it is all too easy
to encrypt something into oblivion.

EOF