def is_valid(visited, n, depth) :
    for i in range(depth) :
        if visited[i] == visited[depth] or abs(visited[i]-visited[depth]) == depth-i :
            return False
    return True
        
def n_queen(visited, n, depth) :
    if depth == n :
        #print(f"배치 완료 : {visited}")
        return 1

    cnt = 0
    for col in range(n) : 
        visited[depth] = col  
        if is_valid(visited, n, depth) :
            #print(f"depth={depth}, col={col}, visited={visited}")
            cnt += n_queen(visited, n, depth+1)
    return cnt
        
def solution(n):
    visited = [-1]*n
    return n_queen(visited, n, 0)
