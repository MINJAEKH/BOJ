def tsp(cnt, now_cost, current) :
    global min_cost

    if cnt == n and w[current][0] != 0 :
        min_cost = min(min_cost, now_cost+w[current][0])
        return

    if min_cost < now_cost :
        return 
    
    for i in range(n) :
        if not visited[i] and w[current][i] != 0 :
            visited[i] = True
            tsp(cnt+1, now_cost+w[current][i], i)
            visited[i] = False

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n
min_cost = float('inf')

visited[0] = True
tsp(1,0,0)
print(min_cost)