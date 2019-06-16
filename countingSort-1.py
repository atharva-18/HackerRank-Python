#!/bin/python3

# Complete the countingSort function below.
def countingSort(arr):
    count = [0]*100
    for i in arr:
        count[i] += 1
    return count

n = int(input())
arr = list(map(int, input().rstrip().split()))

print(*countingSort(arr))
