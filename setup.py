#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:31:40 2022

@author: loldebyte
"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("optimised_roulette.pyx")
)
