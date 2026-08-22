from collections import deque

def solution(n, computers):
    answer = 0
    visited= [False]*n
    
    for i in range(n) :
        if not visited[i] :
            visited[i] = True
            q = deque([i])
        
            while q :
                k = q.popleft()
                for j in range(n) :
                    if computers[k][j] == 1 and not visited[j] :
                        visited[j] = True
                        q.append(j)
            answer += 1
    return answer