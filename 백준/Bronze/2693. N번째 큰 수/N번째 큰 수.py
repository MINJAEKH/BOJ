T = int(input())

for  _ in range(T) :
    arr = []
    arr = list(map(int, input().split()))
    arr.sort()
    print(arr[-3])