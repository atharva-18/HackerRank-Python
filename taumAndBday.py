#!/bin/python

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):
    if z < wc-bc:
        return b*bc+w*(bc+z)
    elif z < bc-wc:
        return b*(wc+z)+w*wc
    else:
        return b*bc+w*wc    

t = int(input())

for t_itr in range(t):
    bw = input().split()

    b = int(bw[0])

    w = int(bw[1])

    bcWcz = input().split()

    bc = int(bcWcz[0])

    wc = int(bcWcz[1])

    z = int(bcWcz[2])

    print(taumBday(b, w, bc, wc, z))
