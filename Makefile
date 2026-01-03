# ------------------------------------------------------------------------
# Makefile for the bluepoint python encryption module.
#
# Sat 03.Jan.2026   Python 2 phased out
#

all:
	@echo Targets: build test git clean

bdate:
	python bdate.py >ext/bdate.h

bluepy3_c.so: ext/bluepy_c.c  ext/bluepoint2.c
	@python3 buildme3.py

# Building modules:
build: bluepy3_c.so

test: build
	@echo Diffs should be silent
	@python3 ./blueencfile.py -e -f -p 1111 Makefile aa
	@python3 ./blueencfile.py -d -f -p 1111 aa bb
	@-diff Makefile bb
	@rm -f aa bb cc dd ee

# These generate files for the dieharder test
genfile: build
	dd  if=/dev/zero of=testfile.bin bs=512 count=10
	@python3 ./bluefile.py -e -f -p 1111 testfile.bin testfile.enc

pseudo:
	dd  if=/dev/random of=pseudo.rnd bs=512 count=10

git:
	@git add .
	@-git commit -m autocheck
	@git push

clean:
	@rm -f aa bb cc dd ee
	@rm -f *.o
	@rm -f *.so
	@rm -f *.pyd
	@rm -f *.dll
	@rm -f *.pyc
	@rm -rf *.egg-info
	@rm -rf __pycache__/
	@rm -rf ./build/*

# EOF