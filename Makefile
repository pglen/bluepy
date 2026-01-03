# ------------------------------------------------------------------------
# Makefile for the bluepoint python module.
#
# Sat 03.Jan.2026   Python 2 phased out

all:
	@echo Targets: build test git clean

#	@echo Targets: build build3 test test3 git clean deb

bdate:
	python bdate.py >bdate.h

bluepy2_c.so:  bluepy_c.c bluepoint2.c
	@#export APPLY_LP2002043_UBUNTU_CFLAGS_WORKAROUND=""
	@python2 buildme.py
	@#python2 setup.py build_ext --inplace

bluepy3_c.so: bluepy_c.c  bluepoint2.c
	@python3 buildme3.py
	@#python setup.py build_ext --inplace

# Building modules:
build2: bluepy2_c.so

build: bluepy3_c.so

# Testing modules:
test2: build2
	@echo Diffs should be silent
	@python2 bluetest2.py >cc
	@python2 bluefile2.py -e -f -p 1111 Makefile aa
	@python2 bluefile2.py -d -f -p 1111 aa bb
	@diff Makefile bb
	@rm -f aa bb cc dd ee

test: build
	@echo Diffs should be silent
	@python3  bluetest.py >cc
	@python3 ./bluefile.py -e -f -p 1111 Makefile aa
	@python3 ./bluefile.py -d -f -p 1111 aa bb
	diff Makefile bb
	@rm -f aa bb cc dd ee

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