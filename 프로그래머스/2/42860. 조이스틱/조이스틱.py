
def solution(name):
    answer = 0
    n = len(name)
    
    # 알파벳 상하 이동
    for alphabet in name:
        answer += min(ord(alphabet) - ord('A'), ord('Z') - ord(alphabet) + 1)
    
    # 커서 좌우 이동
    min_move = n - 1  # 기본값: 오른쪽으로 끝까지 이동
    
    for i in range(n):
        # i 위치 바로 다음부터 연속된 A의 개수 세기
        cnt = 0
        while i + 1 + cnt < n and name[i + 1 + cnt] == 'A':
            cnt += 1
            
        back_dist = i + 1 + cnt
        
        min_move = min(
            min_move,
            i * 2 + (n-back_dist),
            (n-back_dist) * 2 + i
        )
        
    return answer + min_move