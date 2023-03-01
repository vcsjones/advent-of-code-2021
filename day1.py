#!/usr/bin/env python

from common import *
from itertools import *

with open(input_path('day1-input.txt'), 'r') as file:

    nums = map(lambda n: int(n), file.readlines())
    part1 = len(list(filter(lambda n: n[0] < n[1], pairwise(nums))))
    print(f'Part 1: {part1}')