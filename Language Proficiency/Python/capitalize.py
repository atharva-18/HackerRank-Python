#!/bin/python

# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

s = input()
print(solve(s))
