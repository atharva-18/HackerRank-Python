#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    i = ' '*n
    j = '#'*n
    for k in range(1, n+1):
        print(i[k:]+j[:k])

if __name__ == '__main__':
    n = int(input())

    staircase(n)
