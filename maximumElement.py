# Enter your code here. Read input from STDIN. Print output to STDOUT

stack = [0]

N = int(input())

for i in range(N):
    query = list(map(int, input().rstrip().split()))
    if query[0] == 1:
        stack.append(max(query[1], stack[-1]))
    elif query[0] == 2:
        stack.pop()
    else:
        print(stack[-1])
