#!/bin/python3
import itertools
# Complete the getWays function below.

def getWays(n, c):
    hi = int(n/min(c))
    result = [seq for i in range(hi,0,-1) for seq in itertools.combinations_with_replacement(c,i) if sum(seq) == n]
    return len(result)

nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'

print(getWays(n, c))
