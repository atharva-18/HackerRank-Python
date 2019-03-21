#!/bin/python3

# Complete the minimumDistances function below.
def minimumDistances(a):
    dist = {}
    for i in a:
        if i in dist:
            continue
        else:
            if a.count(i) == 2:
                indices = []
                index = 0
                for j in a:
                    if j == i:
                        indices.append(index)
                    index += 1
                dist[i] = abs(indices[0]-indices[1])
    vals = dist.values()
    return print(min(vals,default=-1)) 

n = int(input())

a = list(map(int, input().rstrip().split()))

minimumDistances(a)
