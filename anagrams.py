#!/bin/python3

# Complete the anagram function below.
def anagram(s):
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    if len(s1) != len(s2):
        return "-1"
    cost = 0
    s1_list = list(s1)
    for i in s2:
        if i in s1:
            s1_list.remove(i)
        else:
            cost += 1 
    return len(s1_list) + cost

T = int(input())

for _ in range(T):
    s = input()

    print(anagram(s))