#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:11:38 2022

@author: loldebyte
"""
import pytest
import roulette


@pytest.fixture
def mock_roll():
    rolls = [k for k in range(38)]
    def mocked():
        return rolls.pop(0)
    yield mocked
    

class TestRoll():
    def test_roll(self):
        val = roulette.roll()
        assert val < 38 and val >= 0

def mock_roll_in_test(func):
    def inner(monkeypatch, mock_roll):
        monkeypatch.setattr(roulette, "roll", mock_roll)
        return func()
    return inner

@mock_roll_in_test
def test_roll_n_times_10():
    assert roulette.roll_n_times(10) == 10

@mock_roll_in_test
def test_roll_n_times_37():
    assert roulette.roll_n_times(37) == 37

@mock_roll_in_test
def test_roll_until_full_set():
    assert roulette.roll_until_full_set() == 37

@mock_roll_in_test
def test_roll_until_0_remain():
    assert roulette.roll_until_x_remain(0) == 37

@mock_roll_in_test
def test_get_unrolled_from_37_rolls():
    assert roulette.get_unrolled_from_n_rolls(37) == 0

@mock_roll_in_test
def test_get_unrolled_from_17_rolls():
    assert roulette.get_unrolled_from_n_rolls(17) == 20
