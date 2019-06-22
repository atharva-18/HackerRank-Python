#!/bin/python3

def left(arr):
    stack = [1] #Stack of indices
    output = []
    for ind in range(len(arr)):
        while stack and arr[stack[-1]-1] <= arr[ind]:
            stack.pop()
        left = stack[-1] if stack else 0
        stack.append(ind+1)
        output.append(left)
    return output

def right(arr):
    stack = [1] #Stack of indices
    output = []
    for ind in range(len(arr)):
        while stack and arr[stack[-1]-1] <= arr[ind]:
            stack.pop()
        right = len(arr) - stack[-1]  + 1 if stack else 0
        stack.append(ind+1)
        output.append(right)
    return output[::-1]

def solve(arr):
    left_array = left(arr)
    right_array = right(arr[::-1])
    curr_max = 0
    for i in zip(left_array, right_array):
        curr_max = max(curr_max, i[0]*i[1])
    return curr_max

# arr_count = int(input())

# arr = list(map(int, input().rstrip().split()))

arr = [5, 4, 3, 4, 5]

print(solve(arr))
