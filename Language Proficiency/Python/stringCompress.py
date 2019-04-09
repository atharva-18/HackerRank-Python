# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()

list_a = [list(g) for k, g in groupby(s)]

out = [(len(i), int(i[0])) for i in list_a]

print(*out)
