#!/bin/python3

# Complete the fairRations function below.
def fairRations(B):
    count = 0
    odd = False
    index = 0
    for i in range(len(B)):
        if B[i] % 2 == 1:
            if odd:
                count += (i - index) * 2
                odd = False
            else:   
                odd = True
                index = i
    if odd:
        return print("NO")
    else:
        return print(count)

N = int(input())

B = list(map(int, input().rstrip().split()))

fairRations(B)
