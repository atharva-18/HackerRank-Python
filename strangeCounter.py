#!/bin/python3

# Complete the strangeCounter function below.
def strangeCounter(t):
    rem = 3
    while t > rem:
        t = t-rem
        rem *= 2
    return rem-t+1

t = int(input())

print(strangeCounter(t))
