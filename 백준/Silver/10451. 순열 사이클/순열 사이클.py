import sys
input = sys.stdin.readline

def DFS(link, i, visited) :
    visited.append(i)
    if link[i] not in visited :
        DFS(link, link[i], visited)

for _ in range(int(input())) :
    n = int(input())
    cnt = 0
    link = [0]
    link.extend(list(map(int, input().strip().split()))) # append랑 extend 제대로 사용하자 
    visited = []
    for i in range(1, n+1) :
        if i not in visited :
            DFS(link, link[i], visited)
            cnt += 1
    print(cnt)