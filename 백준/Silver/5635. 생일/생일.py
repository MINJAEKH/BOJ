import sys
input = sys.stdin.readline

N = int(input())

birth = []

for _ in range(N) :
    name, day, month, year = input().strip().split()
    birth.append([int(year),int(month),int(day),name])

birth.sort()
#print(birth)
print(birth[-1][-1])
print(birth[0][-1])