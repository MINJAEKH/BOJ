from itertools import combinations

N = int(input())
answer = []

for i in range(N):
    numbers = list(combinations(list(map(int, input().split())), 3))
    score = 0
    for number in numbers:
        tmp = sum(number) % 10
        score = max(score, tmp)
    answer.append((score, i + 1))

answer = sorted(answer, key=lambda x: (-x[0], -x[1]))
print(answer[0][1])
