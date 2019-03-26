card={}
for _ in range(int(input())):
    name = input()
    score = float(input())
    card[name] = score 

scores = card.values()
second = sorted(list(set(scores)))[1]
second_lowest=[]

for key,value in card.items():
    if value==second:
        second_lowest.append(key)
second_lowest.sort()

for name in second_lowest:
    print(name)
