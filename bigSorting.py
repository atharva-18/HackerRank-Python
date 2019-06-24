#!/bin/python3

# Complete the bigSorting function below.
def bigSorting(arr):
    arr.sort(key=int)
    for i in arr:
        print(i)    

n = int(input())

unsorted = []

for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

bigSorting(unsorted)
