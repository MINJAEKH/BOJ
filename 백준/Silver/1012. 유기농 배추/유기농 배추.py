from collections import deque

def bfs(m, n, cabbages) :
    q = deque()

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0

    for row in range(n) :
        for col in range(m) :
            if cabbages[row][col] == 1 :
                cabbages[row][col] = 0
                q.append((row, col))
                while q :
                    x, y = q.popleft()
                    
                    for i in range(4) :
                        nx, ny = x + dx[i], y + dy[i]

                        if 0 <= nx < n and 0 <= ny < m and cabbages[nx][ny] == 1 :
                            q.append((nx, ny))
                            cabbages[nx][ny] = 0
                cnt += 1
    return cnt

for _ in range(int(input())) :
    m, n, k = map(int, input().split())
    cabbages = [[0]*m for _ in range(n)]

    for _ in range(k) :
        y, x = map(int, input().split())
        cabbages[x][y] = 1

    result =  bfs(m, n, cabbages)
    print(result)