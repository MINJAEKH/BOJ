import sys
input = sys.stdin.readline

from collections import deque, defaultdict

def bfs(graph) :
    visited = {1}
    q = deque([1])
    result = 0

    while q :
        node = q.popleft()
        for next_node in graph[node] : # 2.5
            if next_node not in visited :
                q.append(next_node)
                visited.add(next_node)
                result += 1
    return result

n = int(input()) # 컴퓨터 수
vertices = int(input()) # 컴퓨터 쌍의 수

graph = {i : [] for i in range(1,n+1)}
for _ in range(vertices) :
    e1, e2 = map(int, input().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

print(bfs(graph))