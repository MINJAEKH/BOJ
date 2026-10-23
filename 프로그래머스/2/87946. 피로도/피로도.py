def backtracking(k, n, dungeons, visited) : 
    answer = 0
    
    for i in range(len(dungeons)) :
        required, consumed = dungeons[i]
        
        if k >= required and visited[i] == False :
            visited[i] = True
            answer = max(answer, backtracking(k-consumed, n, dungeons, visited)+1)
            visited[i] = False
    return answer

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False]*len(dungeons)
    
    return backtracking(k, n, dungeons, visited)
    