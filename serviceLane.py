#!/bin/python3

# Complete the serviceLane function below.
def serviceLane(n, width, cases):
    for i in cases:
        route = width[i[0]:i[1]]
        print(min(route))

nt = input().split()

n = int(nt[0])

t = int(nt[1])

width = list(map(int, input().rstrip().split()))

cases = []

for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))

serviceLane(n, width, cases)
