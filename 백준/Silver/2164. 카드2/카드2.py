from collections import deque

n = int(input())
queue = deque(list(i for i in range(1, n+1)))

while len(queue) > 1 :
    queue.popleft()
    behind = queue.popleft()
    queue.append(behind)

print(queue.pop())