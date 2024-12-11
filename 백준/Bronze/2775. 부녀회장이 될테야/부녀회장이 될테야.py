#import sys
#input = sys.stdin.readline

dp = [[0]*15 for _ in range(15)]

for b in range(1,15) :
    dp[0][b] = b

for a in range(1,15) :
    for b in range(1,15) :
        dp[a][b] = dp[a-1][b] + dp[a][b-1]

for _ in range(int(input().strip())) :
    k = int(input())
    n = int(input())
    print(dp[k][n])