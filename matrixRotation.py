#!/bin/python3

# Complete the matrixRotation function below.
def getLayer(i, j, m, n):
    if m%2==0 and n%2==0:
        layer = max(abs(i-m/2),abs(j-n/2))
        if (j<=n-i and i<=m/2) or (i<=m-j and j<=n/2):
            return layer + 1
        else:
            return layer
    else: 
        center_i = (m-1)/2 + 1
        center_j = (n-1)/2 + 1
        layer = max(abs(i-center_i), abs(j-center_j))
        return layer+1

def updateElementPos(i, j, m, n, r, layer):
    while r != 0:
        if i == m and j == n and layer != 0:
            i -= 1
            r -= 1
        elif i==m and j+1<=n:
            j += 1
            r -= 1
        elif i+1<m and m-j>0:
            i += 1
            r -= 1
        elif m>m-i>0 and j==n:
            i -= 1
            r -= 1
        elif m==i and j<=n and layer != 0:
            j -= 1
            r -= 1
        else:
            break
    return i, j

def matrixRotation(matrix, r):
    m, n = len(matrix), len(matrix[0]) 
    if r==0 or (m==1 and n==1):
        return print(matrix)
    perimeter = n*2 + 2*(m - 2)
    if r > perimeter:
        r = r % perimeter
    rotated_mat = [[0 for i in range(m)] for j in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            layer = int(getLayer(i+1, j+1, m, n)) - 1
            m_elem = m - layer
            n_elem = n//2 + layer
            rotated_mat[i][j] = (m_elem, n_elem)
            # i_elem, j_elem = updateElementPos(i, j, m_elem, n_elem, r, layer)
            # rotated_mat[i_elem][j_elem] = matrix[i][j]
    return rotated_mat

# if __name__ == '__main__':
#     mnr = input().rstrip().split()

#     m = int(mnr[0])

#     n = int(mnr[1])

#     r = int(mnr[2])

#     matrix = []

#     for _ in range(m):
#         matrix.append(list(map(int, input().rstrip().split())))

#     matrixRotation(matrix, r)

matrix = [[1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]]
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2], [3, 4]]
r = 1
output = matrixRotation(matrix, r)

for i in range(len(output)):
    print(output[i])

