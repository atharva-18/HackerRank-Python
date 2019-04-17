#!/bin/python3

# Complete the diagonalDifference function below.
def diagonalDifference(n, arr):
    diag_1 = 0
    diag_2 = 0
    for i in range(n):
        diag_1 += arr[i][i]
        diag_2 += arr[i][n-1-i]
    return abs(diag_1-diag_2)

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

print(diagonalDifference(n, arr))
