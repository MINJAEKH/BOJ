from collections import deque

def solution(numbers, target):
    q = deque([0])
    
    for num in numbers :
        for _ in range(len(q)) : 
            before = q.popleft()
            q.append(before + num)
            q.append(before - num)    
            
    return q.count(target)