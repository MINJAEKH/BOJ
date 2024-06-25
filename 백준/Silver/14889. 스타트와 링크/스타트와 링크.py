from itertools import combinations,permutations

N = int(input())
S = []

for i in range(N) :
    S.append(list(map(int, input().split())))

player = [i for i in range(N)]
comb = list(combinations(player, N//2))

min_diff = float('inf')

def get_capacity(team) :
    capacity = 0
    per = list(permutations(team , 2))
    for p in per :
        i = p[0] ; j = p[1]
        capacity += S[i][j]

    return capacity

for i in range(len(comb)) :
    start = list(comb[i])
    link = [x for x in player if x not in start ]
    min_diff = min(min_diff, abs(get_capacity(start) - get_capacity(link)))

print(min_diff)