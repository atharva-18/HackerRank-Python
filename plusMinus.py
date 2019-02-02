#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    pos = 0
    neg = 0
    zer = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] == 0:
            zer += 1
        else:
            neg += 1
    print(round(pos/n, 6))
    print(round(neg/n, 6))
    print(round(zer/n, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
