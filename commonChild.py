#!/bin/python3

# Complete the commonChild function below.
def commonChild(s1, s2 ,m, n):
    L = [[0]*(n + 1) for i in range(m + 1)] 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif s1[i-1] == s2[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
    return L[m][n]
                
s1 = input()

s2 = input()

print(commonChild(s1, s2, len(s1), len(s2)))
