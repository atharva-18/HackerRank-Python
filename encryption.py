#!/bin/python3

# Complete the encryption function below.
def createMat(s, row, col):
    mat = ['']*row
    string = ''
    count = 0
    index = 0
    s = s + ' '*((row*col)-len(s))
    for i in s:
        string += i
        count += 1
        if count == col:
            mat[index] = string
            string = ''
            count = 0
            index += 1
    return mat

def printMat(mat, row, col):
    matrix = [list(i) for i in zip(*mat)]
    out = ''
    for i in matrix:
        output = "".join(i)
        output = output.replace(" ", "")
        out += output + " "
    print(out)

def encryption(s):
    row = int(len(s)**0.5)
    col = row + 1
    while row*col < len(s):
        row += 1
    mat = createMat(s, row, col)
    return printMat(mat, row, col)

s = input()

s = s.replace(' ', '')

encryption(s)
