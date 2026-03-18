def is_valid(row, n, visited) :
    for i in range(row) : 
        if visited[i] == visited[row] or abs(visited[row] - visited[i]) == row - i :
            return False
    return True

def n_queen(depth, n, visited) :
    if depth == n :
        #print(f"배치 완료 : {visited}")
        return 1
    
    cnt = 0
    for col in range(n) :
        visited[depth] = col
        #print(f"depth={depth}, col={col}, visited={visited}")
        if is_valid(depth, n, visited) :
            cnt += n_queen(depth+1, n, visited) 
    
    return cnt

def solution(n):
    visited = [-1]*n    
    answer = n_queen(0, n, visited)
    
    return answer