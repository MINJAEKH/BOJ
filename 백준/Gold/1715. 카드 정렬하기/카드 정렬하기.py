import heapq

n = int(input())
card = [int(input()) for _ in range(n)]
heapq.heapify(card)
ans = 0

while len(card) != 1 :
    first = heapq.heappop(card) # 가장 작은 값 1
    second = heapq.heappop(card) # 가장 작은 값 2
    result = first + second
    ans += result 
    
    heapq.heappush(card, result) # 비교 횟수 결과를 힙에 입력 
    
print(ans)