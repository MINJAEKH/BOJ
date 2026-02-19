stacks = []
result = 0

for _ in range(int(input())) : 
    num = int(input())
    if num == 0 :
        stacks.pop()
        continue
    stacks.append(num)

print(sum(stacks))