from collections import deque

n, k = map(int, input().rstrip().split())
circular_q = deque(list(range(1, n+1)))
result = []

while circular_q :
    for _ in range(k-1) :
        num = circular_q.popleft()
        circular_q.append(num)
    result.append(str(circular_q.popleft()))

print('<'+', '.join(result)+'>')