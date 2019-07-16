#!/bin/python3

# Complete the surfaceArea function below.
def surfaceArea(A, H, W):
    area = 0
    for i in range(H):
        for j in range(W):
            if j == 0:
                if i == H - 1 and j == W - 1 and len(A) == 1: # single block
                    area += 4*A[i][j]
                elif i == 0 and j == W - 1 and len(A[0]) == 1: # vertical top end
                    area += 3*A[i][j]
                elif i == H - 1 and j == W - 1 and len(A[0]) == 1: # vertical bottom end
                    area += 3*A[i][j] + abs(A[i][j] - A[i-1][j])
                elif j == W - 1 and len(A[0]) == 1: # vertical block middle part
                    area += 2*A[i][j] + abs(A[i][j] - A[i-1][j])
                elif i == H - 1 and len(A) == 1: # horizontal left end
                    area += 3*A[i][j]
                elif i == 0: # regular block left side corners
                    area += 2*A[i][j]
                elif i == H - 1:
                    area += 2*A[i][j] + abs(A[i][j] - A[i-1][j])
                else:                      # regular block left middle part
                    area += A[i][j] + abs(A[i][j] - A[i-1][j])
            elif j == W - 1:
                if i == H - 1 and len(A) == 1: # horizontal right end
                    area += 3*A[i][j] + abs(A[i][j] - A[i][j-1])
                elif i == 0:
                    area += 2*A[i][j] + abs(A[i][j] - A[i][j-1]) # regular top right corner
                elif i == H - 1:
                    area += 2*A[i][j] + abs(A[i][j] - A[i][j-1]) + abs(A[i][j] - A[i-1][j])
                else:
                    area += A[i][j] + abs(A[i][j] - A[i][j-1]) + abs(A[i][j] - A[i-1][j])
            else:
                if i == H - 1 and len(A) == 1: # horizontal middle part
                    area += 2*A[i][j] + abs(A[i][j] - A[i][j-1])
                elif i == 0:
                    area += A[i][j] + abs(A[i][j] - A[i][j-1])
                elif i == H - 1:
                    area += A[i][j] + abs(A[i][j] - A[i][j-1]) + abs(A[i][j] - A[i-1][j])
                else:
                    area += abs(A[i][j] - A[i][j-1]) + abs(A[i][j] - A[i-1][j])
            #print("----->", A[i][j])
            area += 2
    return area

HW = input().split()

H = int(HW[0])

W = int(HW[1])

A = []

for _ in range(H):
    A.append(list(map(int, input().rstrip().split())))

print(surfaceArea(A, H, W))
