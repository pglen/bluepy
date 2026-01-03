import os, sys
import setuptools

c_module = setuptools.Extension(
    'bluepy3',
    sources=['bluepoint2.c', 'bluepy_c.c'],
    # extra_compile_args=['-Wall', '-pedantic', '-O2'],
    # libraries=['m']
)

classx = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ]

includex = [ "*", ]

deplist = []
loc_vers =  '1.0.0'     # Default

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Get version number from the main file:
fp = open("bluepy_c.c", "rt")
vvv = fp.read(); fp.close()
loc_vers =  '1.0.0'     # Default
for aa in vvv.split("\n"):
    idx = aa.find("version[]")
    if idx >= 0:        # At the beginning of line
        try:
            #print("line:", aa.split())
            loc_vers = aa.split()[4].replace('"', "")
            loc_vers = loc_vers.replace(';', "")
            break
        except:
            #print("Cannot find version file.")
            pass
#print("loc_vers:", loc_vers)
#sys.exit(1)

setuptools.setup(
    name="bluepy3",
    version=loc_vers,
    author="Peter Glen",
    author_email="peterglen99@gmail.com",
    description="Python encryption bluepy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #url="https://github.com/pglen/pyedpro",
    classifiers=classx,
    include_package_data=True,
    packages=setuptools.find_packages(include=includex),
    scripts = ['bluetest.py', 'bluefile.py',],
    ext_modules=[c_module],
    package_dir = { },
    package_data= { },
    data_files = [ ],

    python_requires='>=3',
    install_requires=deplist,
    entry_points={
        'console_scripts': [
            "bluetest=bluetest:mainfunct",
            "bluefile=bluefile:mainfunct",
            ],
    },
)

