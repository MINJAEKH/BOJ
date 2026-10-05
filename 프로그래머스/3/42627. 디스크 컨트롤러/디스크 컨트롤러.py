import heapq

def solution(jobs):
    heap = []
    curr_time = 0 # 현재 시각
    i = 0       # 힙에 넣을 jobs의 인덱스
    done = 0    # 처리한 작업 개수
    answer = 0
    n = len(jobs)
    
    heapq.heapify(heap)
    jobs.sort(key = lambda x : x[0]) # 작업 요청 시점을 기준으로 정렬
    
    while done < n : 
        # 현재 시각 이전에 요청들어온 작업
        while i < n and jobs[i][0] <= curr_time :
            heapq.heappush(heap, (jobs[i][1], jobs[i][0])) # (소요시간, 요청시간)
            i += 1  # 이미 heap에 들어간 작업은 고려X
        
        if heap :
            processing, request = heapq.heappop(heap)
            curr_time += processing
            answer += (curr_time - request)
            done += 1
        else :
            curr_time += 1
            
    return answer // n