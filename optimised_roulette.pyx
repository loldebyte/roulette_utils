#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:31:01 2022

@author: loldebyte
"""
import random
import cython

def roll() -> int:
    return random.randint(0, 36)

def roll_until_full_set() -> int:
    cdef int number_of_rolls
    rolled = set()
    to_roll = set(range(37))
    number_of_rolls = 0
    while rolled != to_roll:
        rolled.add(roll())
        number_of_rolls += 1
    return number_of_rolls
