#!/bin/python3

# Complete the kFactorization function below.
def kFactorization(n, A):
    while True:
        if len(A) == 0:
            return "-1"
        x = A[-1]
        y = n / x
        if y == 1:
            return [1, int(x)]
        if (n / x) % 1 == 0:
            res = kFactorization((n/x), A)
            return res + [int(n)] if res != "-1" else "-1"
        else:
            A.pop()

nk = input().split()

n = int(nk[0])

k = int(nk[1])

A = sorted(list(map(int, input().rstrip().split())))

result = kFactorization(n, A)

if result == "-1":
    print("-1")
else:
    print(*result)