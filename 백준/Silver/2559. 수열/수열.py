import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int,input().split()))

cum = [0] # 1차 실패 원인 : 처음 k개의 합을 나타내기 위해서는 0이 반드시 필요!  
res = 0
max_sum = float('-inf')

for temp in temperature :
    res += temp
    cum.append(res)

for i in range(k,n+1) :
    curr_sum = cum[i] - cum[i-k]
    max_sum = max(max_sum, curr_sum)

print(max_sum)