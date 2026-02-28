from collections import deque

def solution(begin, target, words): 
    q = deque([(begin, 0)])
    visited = set()
    
    while q : 
        # print(f"q:{q}")
        from_word, cnt = q.popleft()
        
        if from_word == target :
            return cnt 
        
        visited.add(from_word)
        
        for i, to_word in enumerate(words) : 
            if to_word in visited : 
                continue
                
            diff = 0
            for j in range(len(from_word)) :
                if from_word[j] != to_word[j] :
                    diff += 1
            if diff == 1 :
                q.append([to_word, cnt+1]) 
          
    return 0