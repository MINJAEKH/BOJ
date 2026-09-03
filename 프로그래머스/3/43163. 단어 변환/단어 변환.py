from collections import deque

def solution(begin, target, words):
    if target not in words :
        return 0
    
    q = deque([(begin, 0)])
    visited = set([begin])
    answer = 0
    
    while q :
        curr_word, step = q.popleft()
        
        if curr_word == target :
            return step
        
        for word in words :
            if word not in visited : 
                diff = sum(1 for a, b in zip(word, curr_word) if a != b)
                if diff == 1 :
                    visited.add(word)
                    q.append((word, step+1))
