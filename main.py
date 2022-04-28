#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:39:31 2022

@author: loldebyte
"""
import roulette
import argparse
import statistics
import sys


def get_args():
    parser = argparse.ArgumentParser(description="A program that simulates "
                                     "roulette rolls to estimate probabilities")
    parser.add_argument("-n", "--number",
                        help="In mode 'roll', the number of rolls to do.\n"
                        "In mode 'until', the number of remaining unrolled numbers to aim for.",
                        required=True, type=int)
    parser.add_argument("-m", "--mode", help="What kind of simulation should be run, "
                        "supported are :\n"
                        " - 'roll' to count average # of unrolled numbers after n rolls\n"
                        " - 'until' to count average # of rolls to have n "
                        "remaining unrolled numbers.\n"
                        " - 'roll_percent' to count %% of series of n rolls"
                        "that have k or more unrolled numbers\nDefaults to 'roll'.\n",
                        default="roll")
    parser.add_argument("-p", "--precision", help="How many rolls to simulate.",
                        type=int, default=100000)
    parser.add_argument("-u", "--unrolled", type=int, help="The number of unrolled "
                        r"numbers to look for in 'roll_percent' mode. Must be "
                        "omitted in other modes.")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args.mode, args.number, args.precision, args.unrolled

def main():
    mode, n, p, unrolled = get_args()
    if mode == "roll" and unrolled is None:
        vals = [roulette.roll_n_times(n) for _ in range(p)]
        print(f"Mean number of unique numbers rolled in a series of {n} rolls:\n"
              f"{statistics.mean(vals)}")
    elif mode == "until" and n <= 37 and n > 0 and unrolled is None:
        vals = [roulette.roll_until_x_remain(n) for _ in range(p)]
        print(f"Mean number of rolls to get {n} remaning unrolled numbers : "
              f"{statistics.mean(vals)}")
    elif mode == "roll_percent" and unrolled <= 37 and unrolled > 0:
        vals = [roulette.roll_n_times(n) for _ in range(p)]
        n_successful = len(list(filter(lambda x: x+unrolled <= 37, vals)))
        print(f"% series where {unrolled} numbers never rolled (series of "
              f"{n} rolls) : {n_successful/p*100} ; avg out of {p} series")
    else:
        raise ValueError(f"mode {mode} not recognized or used with invalid "
                         "arguments, use '-h' to see usage.")

if __name__ == "__main__":
    main()
