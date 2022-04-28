#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:43:54 2022

@author: loldebyte
"""
import random

def roll() -> int:
    return random.randint(0, 36)

def roll_50_times() -> int:
    rolled_numbers = set([roll() for _ in range(50)])
    return len(rolled_numbers)

def roll_n_times(n: int) -> int:
    rolled_numbers = set([roll() for _ in range(n)])
    return len(rolled_numbers)

N_TEST = 100000
N = 80

"""
vals = [roll_50_times() for _ in range(100000)]
print(statistics.mean(vals))
"""

for k in range(5, 9):
    vals = [roll_n_times(N) for _ in range(N_TEST)]
    n_successful = len(list(filter(lambda x: x+k <= 37, vals)))
    print(f"% series where {k} numbers never rolled in a series of {N} rolls : {n_successful/N_TEST*100} ; avg out of {N_TEST} series")
