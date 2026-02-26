from collections import deque

n, k = map(int, input().rstrip().split())
graph = [int(input()) for i in range(n)]
q = deque([0])

def bfs(k, queue) :
    m = 0
    visited= set()

    while queue :
        num = queue.popleft() # 0 # 1
        visited.add(num) # 0, 1
        next = graph[num] # 1 # 3

        m += 1 # 1 # 2
        if next == k :
            return m

        if next not in visited : 
            queue.append(next) # 1 # 3
    return -1

print(bfs(k, q))