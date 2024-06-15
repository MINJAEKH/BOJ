# O(n)
n, k = map(int,input().split())
divisor = []

for i in range(1, n // 2+1) : 
    if n % i == 0 :
        divisor.append(i)
divisor.append(n)

if k > len(div) :
    print(0)
else :
    print(divisor[k-1])
