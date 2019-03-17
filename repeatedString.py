#!/bin/python3

# Complete the repeatedString function below.
def repeatedString(s, n):
    return print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

s = input()

n = int(input())

repeatedString(s, n)
