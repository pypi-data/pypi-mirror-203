from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '1000.0.2'
DESCRIPTION = 'Validate OpenConfig-based configuration of devices.'

# Setting up
setup(
    name="oc-config-validate",
    version=VERSION,
    author="Nowasky",
    author_email="nowasky.jr@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        ]
)

