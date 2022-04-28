#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:37:53 2022

@author: loldebyte
"""
import random


def roll() -> int:
    return random.randint(0, 36)

def roll_n_times(n: int) -> int:
    """Simulates n consecutive roulette rolls and returns the number of unique rolled numbers"""
    rolled_numbers = set([roll() for _ in range(n)])
    return len(rolled_numbers)

def get_unrolled_from_n_rolls(n: int) -> int:
    """Simulates n consecutive roulette rolls and returns the number of unique unrolled numbers"""
    rolled_numbers = set([roll() for _ in range(n)])
    return len({_ for _ in range(37)} - rolled_numbers)

def roll_until_x_remain(x: int) -> int:
    rolled = set()
    number_of_rolls = 0
    while len(rolled)+x < 37:
        rolled.add(roll())
        number_of_rolls += 1
    return number_of_rolls

def roll_until_full_set() -> int:
    rolled = set()
    to_roll = set(range(37))
    number_of_rolls = 0
    while rolled != to_roll:
        rolled.add(roll())
        number_of_rolls += 1
    return number_of_rolls
