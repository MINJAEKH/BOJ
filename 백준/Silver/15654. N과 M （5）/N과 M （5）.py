def backtracking(depth, permutations) :
    if depth == m :
        print(" ".join(map(str, permutations)))
        return 
    
    for i in range(n) :
        if not visited[i] : # 1
            visited[i] = True
            permutations.append(arr[i])
            backtracking(depth+1, permutations)
            visited[i] = False
            permutations.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False]*n
permutations = []

arr.sort() # 사전 순으로 증가해야 하므로 오름차순으로 정렬
backtracking(0, permutations)