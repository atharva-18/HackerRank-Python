#!/bin/python3

#
# Complete the 'dynamicArray' function below.
#

def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    seqList = [[]]*n
    for query in queries:
        if query[0] == 1:
            index = (query[1]^lastAnswer)%n
            seqList[index] = seqList[index] + [query[2]]
        elif query[0] == 2:
            index = (query[1]^lastAnswer)%n
            lastAnswer = seqList[index][query[2]%len(seqList[index])]
            print(lastAnswer)


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

dynamicArray(n, queries)

