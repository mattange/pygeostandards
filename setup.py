# -*- coding: utf-8 -*-
import setuptools
from pygeostandards.info import VERSION, PACKAGENAME

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=PACKAGENAME,
    version=VERSION,
    author="Matteo Angeloni",
    author_email="mattange@gmail.com",
    description="A small package to take care of geographic and other standard information.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattange/"+PACKAGENAME,
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords='ISO country geography nuts currencies'
)

