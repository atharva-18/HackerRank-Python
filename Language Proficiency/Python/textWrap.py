import textwrap

def wrap(string, max_width):
    count = 0
    out = ''
    for i in range(len(string)):
        out += string[i]
        count += 1
        if count == max_width:
            print(out)
            out = ''
            count = 0
    return out

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)