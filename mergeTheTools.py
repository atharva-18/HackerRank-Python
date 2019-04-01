def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        sub_str = string[i:i+k]
        out = ''
        for j in sub_str:
            if j not in out:
                out += j 
        print(out)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)