def backtracking(k, dungeons, visited, cnt) :
    answer = cnt # 현재 탐험한 던전 개수 
    
    for i in range(len(dungeons)) :
        required, consumed = dungeons[i]
        if not visited[i] and k >= required :
            visited[i] = True
            answer = max(answer, backtracking(k-consumed, dungeons, visited, cnt+1))
            # print(f'i -> {i} : visited={visited}, k={k}, cnt={cnt}, answer={answer}')
            visited[i] = False
    return answer 

def solution(k, dungeons):
    visited = [False] * len(dungeons)
    return backtracking(k, dungeons, visited, 0)
