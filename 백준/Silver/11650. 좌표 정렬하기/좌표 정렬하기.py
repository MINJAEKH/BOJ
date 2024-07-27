N = int(input())

coords = [tuple(map(int,input().split())) for _ in range(N)]

coords.sort(key = lambda x : (x[0],x[1]))
for coord in coords:
    print(coord[0], coord[1])