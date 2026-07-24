def solution(name):
    answer = 0
    n = len(name)
    start, end = ord('A'), ord('Z')
    
    # 알파벳 상하 이동
    for alphabet in name :
        answer += min(ord(alphabet)-start, end-ord(alphabet)+1)
    
    # 커서 좌우 이동
    min_move = n - 1
    i = 0
    
    while i < n :
        next_i = i + 1
        while next_i < n and name[next_i] == 'A' :
            next_i += 1
            
        min_move = min(
            min_move,
            i * 2 + (n - next_i),
            (n - next_i) * 2 + i)
        
        i = next_i 
        
    return answer + min_move