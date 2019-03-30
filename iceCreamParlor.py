#!/bin/python3

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    n = len(arr)
    for i in range(n):
        for j in range(1, n):
            if j == i:
                continue
            elif arr[i] + arr[j] == m:
                out = sorted([i+1, j+1])
                return print(*out, sep=" ")

t = int(input())

for t_itr in range(t):
    m = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    icecreamParlor(m, arr)
