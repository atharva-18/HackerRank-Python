#!/bin/python3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    return print(100 - sum(1 + 2 * c[i] for i in range(0, n, k)))

nk = input().split()

n = int(nk[0])

k = int(nk[1])

c = list(map(int, input().rstrip().split()))

jumpingOnClouds(c, k)
