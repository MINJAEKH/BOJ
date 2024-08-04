T = int(input())

def catchflies(arr, m) :
    max_cnt = 0 
    for i in range(n-m+1) : 
        for j in range(n-m+1) : 
            curr_cnt = 0
            for row in range(i, i+m) : 
                for col in range(j, j+m) : 
                    curr_cnt += arr[row][col]    
            max_cnt = max(max_cnt, curr_cnt)

    return max_cnt 

for t in range(1, T+1) :
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = catchflies(arr, m)
    print(f"#{t} {max_cnt}")