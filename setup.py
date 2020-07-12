#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="symphys",
    version="0.1.0",
    description="Basic package for general physical system modeling. Used as a study aid.",
    long_description=long_description,
    url="https://github.com/ajcav/symphys",
    packages=setuptools.find_packages()
)
