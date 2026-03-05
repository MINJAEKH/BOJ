def dfs(i, visited, computers, n) :
    visited.add(i) # {0} # {0,1} # {0,1,2}
    for j in range(n) : # 0,1,2 # 0.1.2
        if j not in visited and computers[i][j] == 1: # 1 # 2
            dfs(j, visited, computers, n)  # dfs(1) # dfs(2)

def solution(n, computers): 
    answer = 0
    visited = set()
    
    for i in range(n) : # 0
        if i not in visited :
            dfs(i, visited, computers, n) # dfs(0)
            answer += 1
            
    return answer