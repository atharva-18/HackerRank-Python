#!/bin/python3
# import string
# Complete the weightedUniformStrings function below.

def weightedUniformStrings(s, queries):
    # chars = string.ascii_lowercase
    # order = list(range(1, 27))
    # wt_dict = dict(zip(chars, order))
    wt_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    weights = set([wt_dict[s[0]]])
    multiplier = 1
    for i in range(1, len(s)):
        weight = wt_dict[s[i]]
        if s[i]==s[i-1]:
            multiplier += 1
        else:
            multiplier = 1
        weights.add(weight*multiplier)
    for q in queries:
        if q in weights:
            print("Yes")
        else:
            print("No")
    return 0

s = input()

queries_count = int(input())

queries = []

for _ in range(queries_count):
    queries_item = int(input())
    queries.append(queries_item)

weightedUniformStrings(s, queries)
