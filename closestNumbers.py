#!/bin/python3

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr = sorted(arr)
    result = []
    min_diff = abs(arr[0] - arr[1])
    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i]
        if diff == min_diff:
            result.extend([arr[i], arr[i+1]])
        elif diff < min_diff:
            result = [arr[i], arr[i+1]]
            min_diff = diff
    return result
        
#Test case 5 is incorrect, so we do not pass n as an argument to closestNumbers.

n = int(input())

arr = list(map(int, input().rstrip().split()))

print(*closestNumbers(arr))
