def dfs(n, i, visited, computers) :
    visited[i] = True
    
    for j in range(n) :
        if computers[i][j] == 1 and not visited[j] :
            dfs(n, j, visited, computers)
    
        
def solution(n, computers):
    answer = 0
    visited = [False]*n
        
        
    for i in range(n) :
        if not visited[i] : #방문하지 않은 노드라면
            dfs(n, i, visited, computers) 
            answer += 1
    return answer