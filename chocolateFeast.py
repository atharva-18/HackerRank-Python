#!/bin/python3

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    w = n//c
    feast = n//c
    while w >= m:
        bought = w//m
        feast += bought
        w = (w - bought*m) + bought
    return feast

t = int(input())

for _ in range(t):
    ncm = input().split()

    n = int(ncm[0])

    c = int(ncm[1])

    m = int(ncm[2])

    print(chocolateFeast(n, c, m))
