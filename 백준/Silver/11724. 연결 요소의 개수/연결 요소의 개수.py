import sys
input = sys.stdin.readline
import queue

def bfs(graph, u, visited) :
    visited.append(u)
    my_queue = queue.Queue()
    my_queue.put(u)

    while not my_queue.empty():
        u = my_queue.get()
        for v in graph[u] :
            if v not in visited :
                visited.append(v)
                my_queue.put(v)
        #print('visited:',visited, 'my_queue :',my_queue)

n, m = map(int, input().strip().split())
graph = {i: [] for i in range(1, n + 1)}
cnt = 0
visited = []

# 인접리스트 
for _ in range(m) : 
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

for u in graph.keys() :
    if u not in visited :
        bfs(graph, u, visited)
        cnt += 1

print(cnt)