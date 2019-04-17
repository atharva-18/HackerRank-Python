#!/bin/python3

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    arr = []
    for i in range(n):
        routes = [abs(i-j) for j in c]
        arr.append(min(routes))
    return sorted(arr)[-1]

nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))

print(flatlandSpaceStations(n, c))
