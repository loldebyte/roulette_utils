#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:48:26 2022

@author: loldebyte
"""
import random
import statistics


def roll() -> int:
    return random.randint(0, 36)

X_TO_LOOK_FOR = [k for k in range(5, 9)]

def roll_until_x_remain(x: int):
    rolled = set()
    number_of_rolls = 0
    while len(rolled)+x < 37:
        rolled.add(roll())
        number_of_rolls += 1
    return number_of_rolls

for x in X_TO_LOOK_FOR:
    vals = [roll_until_x_remain(x) for _ in range(100000)]
    print(f"avg for {x}: {statistics.mean(vals)}")
