#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maximum = None
    minimum = None
    maxcount = 0
    mincount = 0
    for i in scores:
        if maximum == None or minimum == None:
            maximum = i
            minimum = i
        elif i > maximum:
            maximum = i
            maxcount += 1
        elif i < minimum:
            minimum = i
            mincount += 1
        else:
            continue
    return maxcount, mincount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
