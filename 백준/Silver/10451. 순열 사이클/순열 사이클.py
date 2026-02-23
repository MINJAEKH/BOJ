def dfs(permut, node, visited) :
    visited.append(node)
    #print(visited)
    if permut[node] not in visited :
        dfs(permut, permut[node], visited)

for i in range(int(input())) :
    n = int(input())
    permut = [0] + list(map(int, input().rstrip().split()))
    visited = []
    cnt = 0

    for node in range(1, n+1) :
        if node not in visited :
            #print(node,':',permut[node])
            dfs(permut, node, visited)
            cnt += 1
    print(cnt)
