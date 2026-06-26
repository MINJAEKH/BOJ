from collections import deque 

def solution(priorities, location):
    answer = 0
    queue = deque([
        (priority, i) for i, priority in enumerate(priorities)
    ])
    
    while queue :
        process = queue.popleft()
        
        if any(process[0] < q[0] for q in queue) :
            queue.append(process)
        else :
            answer += 1
            
            if process[1] == location :
                return answer