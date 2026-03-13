from collections import deque

def solution(n, edge):
    graphs = {i : [] for i in range(1, n+1)}
    visited = [-1]*(n+1)
    q = deque([1])
    visited[1] = 0
    
    for v1, v2 in edge :
        graphs[v1].append(v2)
        graphs[v2].append(v1)
    
    while q :
        nd = q.popleft()
        
        for next_nd in graphs[nd] :
            if visited[next_nd] == -1 :
                visited[next_nd] = visited[nd] + 1
                q.append(next_nd)
    
    return visited.count(max(visited))