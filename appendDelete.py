   #!/bin/python
# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    desired = ''
    s_len = len(s)
    t_len = len(t)
    for i in range(t_len):
        if t_len < k:
            return print("Yes")
        elif desired == t and k == 0:
            return print("Yes")
        elif desired != t and k == 0:
            return print("No")
        elif i > s_len:
            desired += t[i]
            k -= 1
        elif s[i] == t[i]:
            desired += t[i]
        else:
            desired += t[i]
            k -= 1

s = input()
t = input()
k = int(input())
appendAndDelete(s, t, k)
