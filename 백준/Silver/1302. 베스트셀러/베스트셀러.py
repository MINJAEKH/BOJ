N = int(input()) 
dic = {}

for _ in range(N) :
    book = input()
    if book not in dic :
        dic[book] = 1
    else :
        dic[book] += 1

max_val = max(dic.values())
bestsellers = []
for k, v in dic.items() :
    if v == max_val :
        bestsellers.append(k)
bestsellers.sort()
print(bestsellers[0])