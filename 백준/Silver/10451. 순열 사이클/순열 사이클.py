for i in range(int(input())) :
    n = int(input())
    permut = [0] + list(map(int, input().rstrip().split()))
    visited = set()
    cnt = 0

    for v in range(1, n+1) :
        if v not in visited :
            cnt += 1
            while v not in visited :
                visited.add(v) # 1 
                v = permut[v] # 3
                #print('visited:',visited) 
    print(cnt)