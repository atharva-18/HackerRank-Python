#!/bin/python3

# Complete the cutTheSticks function below.
def cutTheSticks(arr, n):
    while True:
        cut_len = min(arr)
        print(n)
        arr = [x - cut_len for x in arr]
        zero_count = arr.count(0)
        for i in range(zero_count):
            arr.remove(0)
        n = len(arr)
        if len(arr) == 1:
            print(1)
            break

n = int(input())

arr = list(map(int, input().rstrip().split()))

cutTheSticks(arr, n)
