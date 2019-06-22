from collections import defaultdict

def Trie(): return defaultdict(Trie)

def add(trie, word):
    if word == '':
        if len(trie) > 0: 
            # current word is a prefix of a previous word
            return False
        trie[word] = ''
        return True
    if '' in trie:
        # a prefix of the current word is a previous word
        return False
    return add(trie[word[0]], word[1:])
  
N = int(input())
strings = []

for i in range(N):
    s = input()
    strings.append(s)


def test(trie):
    trie = Trie()
    for line in strings:
        line = line.strip()
        if not add(trie, line):
            return line
    return 0

result = test(strings)

if result == 0:
    print("GOOD SET")
else:
    print("BAD SET")
    print(result)
