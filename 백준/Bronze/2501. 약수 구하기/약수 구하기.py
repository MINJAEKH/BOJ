n, k = map(int,input().split())
div = []

for i in range(1, n // 2+1) : 
    if n % i == 0 :
        div.append(i)
div.append(n)

if k > len(div) :
    print(0)
else :
    print(div[k-1])
