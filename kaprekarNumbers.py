#!/bin/python3

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    numbers = []
    for i in range(p, q+1):
        sqr = str(i**2)
        val_1 = int(sqr[(-1)*len(str(i)):])
        try:
            val_2 = int(sqr[:(-1)*len(str(i))])
        except ValueError:
            val_2 = 0
        if val_1 + val_2 == i:
            numbers.append(int(i))
    if len(numbers) > 0:
        print(*numbers)
    else:
        print("INVALID RANGE")

p = int(input())

q = int(input())

kaprekarNumbers(p, q)
