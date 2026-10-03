import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K :
        # 음식이 1개만 남아 K 이상을 만들 수 없는 경우
        if len(scoville) < 2 :
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    return answer