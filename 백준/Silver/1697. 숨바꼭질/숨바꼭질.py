from collections import deque

n, k = map(int, input().split())

queue = deque()
queue.append((0,n))
#visited = [] 
visited = set()

while queue :
    sec, loc = queue.popleft() # BFS

    if loc == k :
        print(sec)
        break
    
    if loc in visited :
        continue
    
    elif 0 <= loc <= 100000 : # 위치 조건
        #visited.append(loc)
        visited.add(loc)
        queue.append((sec + 1, loc * 2))
        queue.append((sec + 1, loc + 1))
        queue.append((sec + 1, loc - 1))
    