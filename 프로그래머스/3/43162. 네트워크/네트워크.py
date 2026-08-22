def dfs(n, i, visited, computers) :
    visited[i] = True
    for j in range(n) :
        if not visited[j] and computers[i][j] == 1 :
            dfs(n, j, visited, computers)
    
def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    for i in range(n) :
        if not visited[i] :
            dfs(n, i, visited, computers)
            answer += 1
    return answer