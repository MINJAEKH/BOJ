import sys
input = sys.stdin.readline

N = int(input())
info = []

for _ in range(N):
    name, day, month, year = input().strip().split()
    if len(month) == 1 :
        birthday = f'{year}-0{month}-{day}'
    if len(day) == 1 :
        birthday = f'{year}-{month}-0{day}'
    info.append([birthday, name])

info.sort(key=lambda x: x[0])
print(info[-1][-1])
print(info[0][-1])