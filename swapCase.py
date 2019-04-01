import string

def swap_case(s):
    lwr_case = string.ascii_lowercase
    upr_case = string.ascii_uppercase 
    lwr_to_upr = dict(zip(lwr_case, upr_case))
    upr_to_lwr = dict(zip(upr_case, lwr_case))
    out = ""
    for i in s:
        if i.islower():
            out += lwr_to_upr[i]
        elif i.isupper():
            out += upr_to_lwr[i]
        else:
            out += i
    return out

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)