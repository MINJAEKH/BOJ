# 풍선팡2

dx = [0, 1, 0, -1]  # 우하좌상
dy = [1, 0, -1, 0]

for t in range(1, int(input())+1) :
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    max_cnt = 0
    
    for i in range(n) :
        for j in range(m) :
            curr_cnt = arr[i][j]
            
            for d in range(4) :
                nx = i + dx[d]
                ny = j + dy[d] 
                
                if 0 <= nx < n and 0 <= ny < m :
                    curr_cnt += arr[nx][ny]
                    
            max_cnt = max(max_cnt, curr_cnt)
    
    print(f'#{t} {max_cnt}')