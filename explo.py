#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 23:40:16 2022

@author: loldebyte
"""
import roulette
import statistics


N = 1000000
vals = [roulette.roll_until_full_set() for _ in range(N)]
print(statistics.mean(vals))
