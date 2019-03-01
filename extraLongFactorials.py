#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def extraLongFactorials(n):
    if n < 2:
        return 1
    return range_prod(1,n)

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
