from collections import deque

def bfs(n, graph, wire) :
    start, end = wire
    
    q = deque([start])
    visited = [False]*(n+1)
    visited[start], visited[end] = True, True # 끊어진 전선은 지나기지 않도록 방문 처리
    cnt = 1
    
    while q :
        curr = q.popleft()
        for nxt in graph[curr] :
            if not visited[nxt] :
                visited[nxt] = True
                q.append(nxt)
                cnt += 1
    return abs(n-cnt-cnt)

def solution(n, wires):
    answer = 1e9
    graph = {i : [] for i in range(1, n+1)}
    
    for v1, v2 in wires :
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for wire in wires :
        result = bfs(n, graph, wire)
        answer = min(answer, result)
        
    return answer