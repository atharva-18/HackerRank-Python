#!/bin/python3

# Complete the pangrams function below.
def pangrams(s):
    chars = set(s)
    if len(chars) == 26:
        return "pangram"
    else:
        return "not pangram"

# s = input()
s = 'We promptly judged antique ivory buckles for the prize'.split()
s = "".join(s)

print(pangrams(s))
