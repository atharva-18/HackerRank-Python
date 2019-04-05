# Enter your code here. Read input from STDIN. Print output to STDOUT
import string

s = input()

def ginorts(s):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    lwr_case = []
    upr_case = []
    even_digits = []
    odd_digits = []
    for i in s:
        if i in lower:
            lwr_case.append(i)
        elif i in upper:
            upr_case.append(i)
        else:
            if int(i)%2 == 0:
                even_digits.append(str(i))
            else:
                odd_digits.append(str(i))
    lwr_case.sort()
    upr_case.sort()
    even_digits.sort()
    odd_digits.sort()
    return "".join(lwr_case) + "".join(upr_case) + "".join(odd_digits) + "".join(even_digits)

print(ginorts(s))
