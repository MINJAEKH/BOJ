import sys
input = sys.stdin.readline
N = int(input())

rank = []
body_info = [tuple(map(int, input().strip().split())) for _ in range(N)]

for i in range(N) :
    k = 0
    for j in range(N) :
        if i == j :
            continue
        if (body_info[i][0] < body_info[j][0]) & (body_info[i][1] < body_info[j][1]) :
            k += 1
    rank.append(k+1)

print(*rank)