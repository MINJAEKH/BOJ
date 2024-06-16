N = int(input())
N_lists = list(map(int, input().split()))

# Sol 1
print(min(N_lists), max(N_lists))

# Sol 2
mini = 1000000
maxi = -1000000
for num in N_lists :
    if num >= maxi : # 20       35
        maxi = num
    if num <= mini : # 20   10      7
        mini = num

print(mini, maxi)
