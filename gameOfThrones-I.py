#!/bin/python3

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    done = []
    even = 0
    odd = 0
    for i in s:
        if i in done:
            continue
        else:
            if s.count(i)%2 == 0:
                even += 1
            else:
                odd += 1
            done.append(i)
    if len(s)%2 == 0:
        if len(done) == even:
            return "YES"
        else:
            return "NO"
    else:
        if odd == 1:
            return "YES"
        else:
            return "NO"

s = input()

print(gameOfThrones(s))
