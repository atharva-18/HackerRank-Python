#!/bin/python3

# Complete the funnyString function below.
def funnyString(s):
    s_char = list(map(ord, s))
    s_diff = []
    for i in range(len(s_char) - 1):
        s_diff.append(abs(s_char[i+1] - s_char[i]))
    if s_diff == s_diff[::-1]:
        return "Funny"
    else:
        return "Not Funny"

n = int(input())

for i in range(n):
    s = input()
    print(funnyString(s))

