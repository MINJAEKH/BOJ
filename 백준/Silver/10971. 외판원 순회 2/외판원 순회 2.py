import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)] 

visited = [False]*n
min_cost = float('inf')

def tsp(node, now_cost, cnt) :
    global min_cost
    
    if cnt == n and w[node][0] > 0:
        min_cost = min(min_cost, now_cost+w[node][0]) # 출발지로
        return 
    
    for col in range(n) :
        if w[node][col] > 0 and not visited[col] :
            visited[col] = True
            tsp(col, now_cost + w[node][col], cnt+1) 
            visited[col] = False 

for i in range(n) :
    visited[i] = True
    start = i
    tsp(i,0,1) 
print(min_cost)