#!/bin/python3

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    maximum = 0
    for i in range(l, r+1):
        for j in range(i, r+1):
            if i^j > maximum:
                maximum = i^j
    return maximum


l = int(input())

r = int(input())

print(maximizingXor(l, r))
