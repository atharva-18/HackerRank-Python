#!/bin/python3

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    s1 = list(s1)
    removed = 0
    for i in s2:
        if i in s1:
            s1.remove(i)
        else:
            removed += 1
    return len(s1) + removed

s1 = input()
s2 = input()
print(makingAnagrams(s1, s2))
