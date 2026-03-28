def backtracking(depth, k, dungeons, visited) :
    answer = depth
    
    for i in range(len(dungeons)) :
        required, used = dungeons[i]
        
        if not visited[i] and k >= required :
            visited[i] = True
            # print(f'i -> {i} : visited={visited}, k={k}, depth={depth}')
            cnt = backtracking(depth+1, k-used, dungeons, visited)
            answer = max(answer, cnt)
            visited[i] = False
            
    return answer

def solution(k, dungeons):
    visited = [False]*len(dungeons)
    
    return backtracking(0, k, dungeons, visited)