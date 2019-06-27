#!/bin/python3

# Complete the cipher function below.

def cipher(k, s, n):
    res = s[0]
    for i in range(1, n):
        if i < k:
            res += str(int(s[i])^int(s[i-1]))
        else:
            res += str(int(s[i])^int(s[i-1])^int(res[i-k]))
    return res


nk = input().split()

n = int(nk[0])

k = int(nk[1])

s = input()

print(cipher(k, s, n))
