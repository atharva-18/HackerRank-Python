#!/bin/python3

# Complete the pangrams function below.
def pangrams(s):
    chars = set(s)
    if len(chars) == 27:
        return "pangram"
    else:
        return "not pangram"

s = input()

print(pangrams(s))
