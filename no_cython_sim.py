#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:37:56 2022

@author: loldebyte
"""
import statistics
import random

def roll() -> int:
    return random.randint(0, 36)

def roll_until_full_set() -> int:
    rolled = set()
    to_roll = set(range(37))
    number_of_rolls = 0
    while rolled != to_roll:
        rolled.add(roll())
        number_of_rolls += 1
    return number_of_rolls

N = 1000000
vals = [roll_until_full_set() for _ in range(N)]
print(statistics.mean(vals))
