#!/bin/python3

import math

# Complete the squares function below.
def squares(a, b):
    return math.floor(b**0.5) - math.ceil(a**0.5) + 1

q = int(input())

for q_itr in range(q):
    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    print(squares(a, b))
