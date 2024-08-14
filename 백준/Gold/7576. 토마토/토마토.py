import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
visited = [[False]*m for _ in range(n)]
#visited = set()
tomato_cnt = 0 

for i in range(n) :
    for j in range(m) :
        if arr[i][j] == 1 :
            queue.append((0,i,j))
            tomato_cnt += 1

        elif arr[i][j] == 0 :
            tomato_cnt += 1

while queue :
    day, x, y = queue.popleft()
    visited[x][y] = True
    
    for d in range(4) : 
        nx = x + dx[d] 
        ny = y + dy[d]
        
        if 0 <= nx< n and 0 <= ny < m :
            if arr[nx][ny] == 0 and visited[nx][ny] == False : 
                arr[nx][ny] = 1
                queue.append((day+1, nx, ny))

empty_cnt = n*m - tomato_cnt
if (tomato_cnt - empty_cnt) == sum([sum(row) for row in arr]) :
    # 0 이 없을 땐 day  = 0
    print(day)
else :
    print(-1)
