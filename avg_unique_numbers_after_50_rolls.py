#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 00:43:54 2022

@author: loldebyte
"""
import random
import statistics


def roll() -> int:
    return random.randint(0, 36)

def roll_50_times() -> int:
    rolled_numbers = set([roll() for _ in range(50)])
    return len(rolled_numbers)

vals = [roll_50_times() for _ in range(100000)]
print(statistics.mean(vals))
