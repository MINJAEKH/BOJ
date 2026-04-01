from collections import deque 

def bfs(graph, n, start, end) :
    q = deque([end])
    cnt = 0 
    visited = [False]*(n+1)
    visited[start], visited[end] = True, True
    
    while q : 
        node = q.popleft() 
        cnt += 1
        for v in graph[node] :
            if not visited[v] : 
                q.append(v)
                visited[v] = True
    return cnt

def solution(n, wires):
    answer = float('inf')
    graph = {i : [] for i in range(1,n+1)}
    
    for s, e in wires :
        graph[s].append(e)
        graph[e].append(s)
        
    for s, e in wires :        
        tower_cnt = bfs(graph, n, s, e)
        diff = abs(tower_cnt - (n - tower_cnt))
        answer = min(answer, diff)
        
    return answer