#!/bin/python3
import string
# Complete the caesarCipher function below.
def caesarCipher(s, k):
    U = string.ascii_uppercase
    L = string.ascii_lowercase
    U_s = U[k%26:] + U[:k%26]
    L_s = L[k%26:] + L[:k%26]
    cipher_U = dict(zip(U, U_s))
    cipher_L = dict(zip(L, L_s))
    cipher = {**cipher_L, **cipher_U}
    result = ''
    for c in s:
        if c in U or c in L:
            result += cipher[c]
        else:
            result += c
    return result

n = int(input())

s = input()

k = int(input())

print(caesarCipher(s, k))
