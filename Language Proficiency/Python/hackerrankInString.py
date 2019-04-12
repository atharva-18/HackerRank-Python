#!/bin/python3

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    sub = "hackerrank"
    i = 0
    for j in s:
        if j == sub[i]:
            i+=1
            if i == len(sub):
                return "YES"
    return "NO"

q = int(input())

for q_itr in range(q):
    s = input()

    print(hackerrankInString(s))
