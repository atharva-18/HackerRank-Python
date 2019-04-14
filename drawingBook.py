#!/bin/python3

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    return min(p//2, n//2 - p//2)

n = int(input().strip())

p = int(input().strip())

print(pageCount(n, p))        
