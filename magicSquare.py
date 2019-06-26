#!/bin/python3

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    magic_perms = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],] # Since 15 is the avg sum of rows/columns/diags of all possible magic squares
    costs = []
    for p in magic_perms:
        curr_cost = 0
        for p_row, s_row in zip(p, s):
            for p_elem, s_elem in zip(p_row, s_row):
                if p_elem != s_elem:
                    curr_cost += abs(p_elem - s_elem) # Cost of converting current element
        costs.append(curr_cost)
    return min(costs)


s = []

for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

print(formingMagicSquare(s))
