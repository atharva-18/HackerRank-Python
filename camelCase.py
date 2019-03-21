#!/bin/python3

import string

# Complete the camelcase function below.
def camelcase(s):
    kw = string.ascii_uppercase
    count = 1
    for i in s:
        if i in kw:
            count += 1
    return count

s = input()

print(camelcase(s))
