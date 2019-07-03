nk = list(map(int, input().rstrip().split()))

n, k = nk[0], nk[1]

imp = []
non_imp = []

for i in range(n):
    lt = list(map(int, input().rstrip().split()))
    if lt[1] == 1:
        imp.append(lt[0])
    else:
        non_imp.append(lt[0])
    
imp.sort(reverse=True)

luck = sum(non_imp)

count = 0   

while(k):
    luck += imp[count]
    count += 1
    k -= 1

print(luck - sum(imp[count:]))
