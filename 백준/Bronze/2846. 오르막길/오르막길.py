N = int(input())

road = list(map(int,input().split()))
max_height= 0
curr_height = 0

for i in range(1,N) :
    if road[i-1] < road[i] :
        curr_height += (road[i] - road[i-1])
        max_height = max(curr_height, max_height)
    else :
        curr_height = 0

print(max_height)            