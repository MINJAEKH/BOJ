import sys
input = sys.stdin.readline

from collections import deque, Counter

c, r = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(r)]

def bfs(r, c, tomatoes) : 
    q = deque()
    days = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    if sum(tomatoes[row].count(0) for row in range(r)) == 0 : 
        return 0
    
    for row in range(r) : 
        for col in range(c) :
            if tomatoes[row][col] == 1 :
                q.append((row, col))

    while q :
        x, y = q.popleft()
 
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and tomatoes[nx][ny] == 0  :
                q.append((nx, ny))
                tomatoes[nx][ny] = tomatoes[x][y] + 1

    result = 0
    for row in tomatoes : 
        for value in row : 
            if value == 0 :
                return -1

            result = max(result, value) 

    return result - 1

print(bfs(r, c, tomatoes))