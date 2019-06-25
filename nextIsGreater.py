def nextPermutation(string):
    N = len(string)
    S = list(string)
    i = N - 1 # i is the first swap imdex
    while i > 0 and S[i-1] >= S[i]:
        i = i - 1
    if i <= 0:
        return False # Current string is the greatest of all possible permutations

    j = N - 1 # j is the second swap index
    while S[j] <= S[i -1]:
        j = j - 1
    S[i-1],S[j] = S[j],S[i-1]

    S[i:] = S[N:i-1:-1] # reverse the part of string following the first swap index

    print("".join(S))
    return True

T = int(input())
for i in range(T):
    s = input()
    res = nextPermutation(s)
    if not res:
        print("no answer")