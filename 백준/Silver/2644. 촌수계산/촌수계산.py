import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().strip().split())
relatives = {i : [] for i in range(1, n+1)}
cnt = 0
visited = []
flag = False 

for _ in range(int(input())) :
    x, y = map(int, input().strip().split())
    relatives[x].append(y)
    relatives[y].append(x)

def dfs(x, cnt, b) :
    global flag 
    visited.append(x)

    if x == b :
        flag = True
        print(cnt)

    for v in relatives[x] :
        if v not in visited :
            #print (v, cnt+1, b)
            dfs(v, cnt + 1, b)
            if flag : 
                return 

dfs(a, 0, b)

if flag == False :
    print(-1)