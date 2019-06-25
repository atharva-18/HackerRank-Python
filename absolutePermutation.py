#!/bin/python3

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    pos = list(range(1, n+1))
    if k == 0:
        print(*pos)
    else:
        for i in reversed(range(len(pos))):
            if pos[i] + k not in pos[i:] and pos[i] + k <= n: 
                pos[i] += k
            elif pos[i] - k not in pos[i:] and pos[i] - k > 0:
                pos[i] -= k
            else:
                print("-1")
                return 0
        print(*pos)
    return 0

t = int(input())

for t_itr in range(t):
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    absolutePermutation(n, k)
