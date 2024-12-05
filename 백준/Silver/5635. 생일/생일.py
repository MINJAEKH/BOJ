from datetime import datetime

N = int(input())

info = []

for _ in range(N):
    name, day, month, year = input().strip().split()
    birthday = datetime(int(year), int(month), int(day))
    info.append([birthday, name])

info.sort(key=lambda x: x[0])
print(info[-1][-1])
print(info[0][-1])