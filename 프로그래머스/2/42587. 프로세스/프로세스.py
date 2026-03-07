from collections import deque 

def solution(priorities, location):
    seq = 0
    q = deque([
        [idx, process] for idx, process in enumerate(priorities)
    ])
    
    while q :
        curr_idx, curr_process = q.popleft()
        
        if any(curr_process < np for ni, np in q) :
            q.append((curr_idx, curr_process))
        else :
            seq += 1
            priorities[curr_idx] = seq
    return priorities[location]