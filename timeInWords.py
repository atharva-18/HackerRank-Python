#!/bin/python3

# Complete the timeInWords function below.
def timeInWords(h, m):
    mins = {1:'one minute', 2:'two minutes', 3:'three minutes', 4:'four minutes', 5:'five minutes', 6:'six minutes', 7:'seven minutes', 8:'eight minutes', 9:'nine minutes', 10:'ten minutes', 11:'eleven minutes', 12:'twelve minutes', 13:'thirteen minutes', 14:'fourteen minutes', 16:'sixteen minutes', 17:'seventeen minutes', 18:'eighteen minutes', 19:'nineteen minutes', 20:'twenty minutes', 21:'twenty one minutes', 22:'twenty two minutes', 23:'twenty three minutes', 24:'twenty four minutes', 25:'twenty five minutes', 26:'twenty six minutes', 27:'twenty seven minutes', 28:'twenty eight minutes', 29:'twenty nine minutes'}
    hours = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve'}
    out = ''
    if m == 0:
        out = hours[h]+" o' clock"
    elif 0<m<15:
        out = mins[m]+" past "+hours[h]
    elif m == 15:
        out = "quarter past "+hours[h]
    elif 15<m<30:
        out = mins[m]+" past "+hours[h]
    elif m == 30:
        out = "half past "+hours[h]
    elif 30<m<45:
        out = mins[60-m]+" to "+hours[h+1]
    elif m == 45:
        out = "quarter to "+hours[h+1]
    elif 45<m<=59:
        out = mins[60-m]+" to "+hours[h+1]
    return print(out)

h = int(input())

m = int(input())

timeInWords(h, m)
