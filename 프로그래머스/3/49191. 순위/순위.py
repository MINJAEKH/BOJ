def solution(n, results):
    answer = 0
    # game_matrix[i][i] == True면 i가 j이김 / False면 j가 i 이김
    game_matrix = [[None] * (n + 1) for _ in range(n + 1)]
    
    for a, b in results :
        game_matrix[a][b] = True
        game_matrix[b][a] = False
    
    for k in range(1, n+1) :
        for i in range(1, n+1) :
            for j in range(1, n+1) :
                if game_matrix[i][k] == True and game_matrix[k][j] == True :
                    game_matrix[i][j] = True
                    game_matrix[j][i] = False
    
    for row in game_matrix :
        if row.count(None) == 2 : # (0,0) + 자기 자신은 제외
            answer += 1
    return answer