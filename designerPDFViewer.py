#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    letters = list(string.ascii_lowercase)
    aDict = dict(zip(letters, h))
    height = 0
    for i in word:
        if aDict[i] > height:
            height = aDict[i]
    return len(word)*height

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
