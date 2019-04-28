from itertools import product

# Enter your code here. Read input from STDIN. Print output to STDOUT
A = map(int, list(input().rstrip().split()))
B = map(int, list(input().rstrip().split()))

prod = list(product(A, B))

print(*prod)
