#!/bin/python

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful = 0
    for i in range(i, j+1):
        n = i
        rev = 0
        while(n>0):
            dig = n%10
            rev = rev*10+dig
            n=n//10
        if (i-rev)%k == 0:
            beautiful += 1
    return beautiful


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = raw_input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
