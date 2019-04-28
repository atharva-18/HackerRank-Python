from itertools import product

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = map(int, input().split())
B = map(int, input().split())

prod = list(product(A, B))

print(*prod)
