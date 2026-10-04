import heapq
from collections import defaultdict

def solution(operations):
    count_map = defaultdict(int)
    min_heap, max_heap = [], []
    answer = []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    
    for op in operations :
        code, value = op.split()
        num = int(value)
        
        if code == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            count_map[num] += 1 
        elif code == 'D' :
            if num == 1 :
                while max_heap and count_map[-max_heap[0]] == 0 :
                    heapq.heappop(max_heap)
                if max_heap :
                    count_map[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
                    
            elif num == -1 : 
                while min_heap and count_map[min_heap[0]] == 0 :
                    heapq.heappop(min_heap)
                if min_heap :
                    count_map[min_heap[0]] -= 1
                    heapq.heappop(min_heap)
    # print(count_map)
    # print(min_heap)
    # print(max_heap)
    
    while min_heap and count_map[min_heap[0]] == 0 :
        heapq.heappop(min_heap)
    while max_heap and count_map[-max_heap[0]] == 0 :
        heapq.heappop(max_heap)
    
    if not min_heap and not max_heap :
        return [0,0]
    else :
        return [-max_heap[0], min_heap[0]]
    return answer