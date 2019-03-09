#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def getLayer(i, j, m):
    if m%2==0:
        layer = abs(max(i-m/2, j-m/2))
        if i>m/2 and j>m/2:
            return layer
        return layer+1
    else: 
        centre_pos = (m-1)/2 + 1
        layer = abs(max(i-centre_pos, j-centre_pos))
        return layer+1

def updateElementPos(i, j, m, n, r):
    while r != 0:
        if i == m and j == n:
            break
        elif i+1<=m and j<=n:
            i += 1
            r -= 1
        elif i==m and j+1<=n:
            j += 1
            r -= 1
        elif i+1<=m and j==n:
            i += 1
            r -= 1
        else:
            j += 1
            r -= 1
    return i, j

def matrixRotation(matrix, r):
    if r==0:
        return matrix
    m = len(matrix)
    n = len(matrix[0])
    peri = (2*m+2*n)
    if peri<r:
        r = r%(peri)
    if int(r)==1:
        return matrix
    # else:
    #     m_range = range
    #     for i in range(len(matrix)):
    #         for j in range(len(i)):

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
