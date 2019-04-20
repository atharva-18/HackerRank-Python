#!/bin/python3

# Complete the superReducedString function below.
def superReducedString(s):
    temp_list = list(s)
    i = 0
    while i < len(temp_list)-1:
        if temp_list[i] == temp_list[i+1]:
            del temp_list[i]
            del temp_list[i]
            i = 0
        else:
            i += 1
    s = ''.join(temp_list)
    if s == '':
        return "Empty String"
    else:
        return s
 
s = input()

result = superReducedString(s)

print(result)
