dp = [[0]*30 for _ in range(30)]
for m in range(1,30) :
    dp[1][m] = m

for n in range(2,30) :
    for m in range(1, 30) :
        dp[n][m] = dp[n-1][m-1] + dp[n][m-1]
        
for _ in range(int(input())) :
    N, M = map(int, input().strip().split())
    print(dp[N][M])