#!/bin/python3
import itertools
# Complete the acmTeam function below.
def acmTeam(topic):
    n = list(range(len(topic)))
    teams = list(itertools.combinations(n, 2))
    max_num = 0
    count = 0
    for i in teams:
        tot = 0
        for j in range(len(topic[0])):
            if topic[i[0]][j] == '1' or topic[i[1]][j] == '1':
                tot += 1
        if tot > max_num:
            max_num = tot
            count = 1
        if tot == max_num:
            count += 1
    print(max_num)
    print(count-1)

nm = input().split()

n = int(nm[0])

m = int(nm[1])

topic = []

for _ in range(n):
    topic_item = input()
    topic.append(topic_item)

acmTeam(topic)
