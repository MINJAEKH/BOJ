import math 

for _ in range(int(input())) :
    n, m = map(int, input().strip().split())
    print(math.comb(m, n))