if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

arr = sorted(set(arr))
print(arr[-2])
