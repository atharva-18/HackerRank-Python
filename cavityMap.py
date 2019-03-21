#!/bin/python3

# Complete the cavityMap function below.
def cavityMap(g, n):
    result = [list(row[:]) for row in g]
    for i in range(1,(n-2)+1):
        for j in range(1,(n-2)+1):
            if grid[i][j]>max(grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]):
                result[i][j]='X'
    for i in range(n):
        print("".join(result[i]))

n = int(input())

grid = []

for _ in range(n):
    grid_item = input()
    grid.append(grid_item)

cavityMap(grid, n)
