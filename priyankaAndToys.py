#!/bin/python3

# Complete the toys function below.
def toys(w):
    containers = 0
    while len(w)>0:
        first = min(w)
        containers += 1
        w = [i for i in w if i > first + 4]    
    return containers

n = int(input())

w = list(map(int, input().rstrip().split()))

print(toys(w))
