from collections import deque
stacked = deque()

for _ in range(int(input())) : #LIFO
    num = int(input())
    
    if num == 0 :
        stacked.pop()    
    else :
        stacked.append(num)

print(sum(stacked))