N = int(input())
N_lists = list(map(int, input().split()))

mini = 1000000
maxi = -1000000
for num in N_lists :
    if num >= maxi :
        maxi = num
    if num <= mini :
        mini = num
print(mini, maxi)
