import sys
input = sys.stdin.readline
import queue
def bfs(i) : # i == start node
    cnt = 0
    my_queue  = queue.Queue()
    my_queue.put(i) 

    for _ in range(n) :
        u = my_queue.get()
        cnt += 1
        if graph[u] == k :
            return cnt
        else :
            my_queue.put(graph[u]) 

    return -1

n, k = map(int, input().strip().split())
graph = [int(input()) for _ in range(n)]

print(bfs(0))