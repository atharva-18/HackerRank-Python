def count_substring(string, sub_string):
    n = len(sub_string)
    count = 0
    strings = 0
    for i in range(len(string)):
        if string[i] == sub_string[count]:
            count += 1
        elif string[i] != sub_string[count]:
            count = 0
        if count == n:
            if string[i] == sub_string[0]:
                count = 1
            else:
                count = 0
            strings += 1
    return strings

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)