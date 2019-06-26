#!/bin/python3

# Complete the stringReduction function below.
def stringReduction(s):
    char_count = {'a':0, 'b':0, 'c':0}
    for i in s:
        char_count[i] += 1
    if char_count['a']%2 == char_count['b']%2 == char_count['c']%2:
        return 2
    elif len(set(s)) == 1:
        return len(s)
    else:
        return 1


t = int(input())

for t_itr in range(t):
    s = input()

    print(stringReduction(s))
