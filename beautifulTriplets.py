#!/bin/python3

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    triplets = 0
    for i in arr:
        if i-d in arr and i+d in arr:
            triplets += 1
    return triplets

nd = input().split()

n = int(nd[0])

d = int(nd[1])

arr = list(map(int, input().rstrip().split()))

print(beautifulTriplets(d, arr))
