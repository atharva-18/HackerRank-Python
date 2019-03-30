#!/bin/python3

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    games = 0
    while s >= 0:
        s -= p
        p = max(p - d, m)
        games += 1
    return games - 1

pdms = input().split()

p = int(pdms[0])

d = int(pdms[1])

m = int(pdms[2])

s = int(pdms[3])

print(howManyGames(p, d, m, s))
