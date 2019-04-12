#!/bin/python3

from math import gcd

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    lo = a[0]
    for i in a[1:]:
        lo = int(lo*i/gcd(lo,i))
    hi = b[0]
    for i in b[1::]:
        hi = int(gcd(hi, i))
    count = 0
    i = 1
    for i in range(lo, hi+1, lo):
        if gcd(i,int(hi)) == i:
            count += 1
    return count

nm = input().split()

n = int(nm[0])

m = int(nm[1])

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

print(getTotalX(a, b))
