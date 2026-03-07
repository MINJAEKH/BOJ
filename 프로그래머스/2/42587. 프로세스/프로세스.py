from collections import deque

def solution(priorities, location):
    q = deque([(p, i) for i, p in enumerate(priorities)])
    sorted_priorities = sorted(priorities, reverse=True)
    answer = 0
    
    while q:
        curr_p, curr_i = q.popleft()
        
        if curr_p < sorted_priorities[answer]:
            q.append((curr_p, curr_i))
        else:
            answer += 1
            if curr_i == location:
                return answer