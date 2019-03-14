#!/bin/python3

# Complete the equalizeArray function below.
def equalizeArray(n, arr):
    return print(min(n - arr.count(i) for i in arr))

n = int(input())

arr = list(map(int, input().rstrip().split()))

equalizeArray(n, arr)
