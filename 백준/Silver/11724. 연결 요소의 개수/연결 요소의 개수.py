### 연결 요소의 개수
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, m= map(int, input().rstrip().split())
graph = {i : [] for i in range(1, n+1)}

for _ in range(m) :
    v, u = map(int, input().rstrip().split())
    graph[v].append(u)
    graph[u].append(v)

visited = set()
q = deque()
result = 0

for i in range(1, n+1) : # 1
    if i not in visited : 
        result += 1
        visited.add(i) # 1
        q.append(i)
        while q :
            v = q.popleft()  
            for u in graph[v] :# 1,2
                if u not in visited : 
                    q.append(u) 
                    visited.add(u)

print(result)