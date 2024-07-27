N = int(input())
coords = [tuple(map(int,input().split())) for _ in range(N)]

sorted_coords = sorted(coords, key = lambda x : (x[0],x[1]))
for coord in sorted_coords:
    print(coord[0], coord[1])