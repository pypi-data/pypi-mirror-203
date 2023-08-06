from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.1.0.1'
DESCRIPTION = 'pygame game-making engine'

# Setting up
setup(
    name="pygameHat",
    version=VERSION,
    author="Wojciech Błajda",
    #author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    install_requires=['pygame', 'pyinstaller'],
    keywords=['python', 'pygame', 'game', 'engine', 'maker', 'tool'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
