#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hh = s[:2]
    mm = s[3:5]
    ss = s[6:8]
    period = s[8:]
    if period == "PM" and hh != "12":
        hh = int(hh) + 12
        hh = str(hh)
    elif period == "AM" and hh == "12":
        hh = "00"
    return hh+":"+mm+":"+ss

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
