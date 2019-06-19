# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())

S = ''

stack = []

for i in range(N):
    op = input().rstrip().split(' ')
    if op[0] == '1':
        stack.append(S)
        S += op[1]
    elif op[0] == '2':
        stack.append(S)
        S = S[:-int(op[1])]
    elif op[0] == '3':
        print(S[int(op[1]) - 1])
    elif op[0] =='4':
        S = stack.pop()
