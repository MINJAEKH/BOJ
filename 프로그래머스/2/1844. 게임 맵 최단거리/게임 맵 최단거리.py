from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    q = deque([(0,0)])
    visited = [[-1]*m for _ in range(n)]
    visited[0][0] = 1
    
    dx = [-1,1,0,0] # 하, 상, 좌, 우
    dy = [0,0,-1,1]

    while q :
        x, y = q.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 :
                if visited[nx][ny] == -1 :
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

    return visited[-1][-1]