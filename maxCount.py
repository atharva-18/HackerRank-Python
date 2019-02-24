def minCount(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 0
        count[i] += 1
        if count[i] == 2:
            del count[i]
    return list(count.keys())[0]

arr = [1, 5, 6, 6, 8, 5, 1]
print(minCount(arr))
