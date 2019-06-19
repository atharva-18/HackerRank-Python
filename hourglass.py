#!/bin/python3

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hg_vals = []
    for i in range(4):
        for j in range(4):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hg_vals.append(top+middle+bottom)
    return max(hg_vals)    
            
arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(hourglassSum(arr))
