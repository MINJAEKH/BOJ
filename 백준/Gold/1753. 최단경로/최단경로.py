import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())

graph = {i: [] for i in range(1, v + 1)}
dist = [float('inf')] * (v + 1)

for _ in range(e):
    n1, n2, w = map(int, input().split())
    graph[n1].append((n2, w))

def dijkstra(start, dist, graph):
    dist[start] = 0
    hp = [(0, start)]  # (비용, 노드)

    while hp:
        curr_cost, node = heapq.heappop(hp)

        if dist[node] < curr_cost:
            continue

        for next_node, weight in graph[node]:
            next_cost = curr_cost + weight

            if dist[next_node] > next_cost:
                dist[next_node] = next_cost
                heapq.heappush(hp, (next_cost, next_node))

    return dist

result = dijkstra(start, dist, graph)
for i in range(1, len(result)):
    if result[i] == float('inf'):
        print('INF')
    else:
        print(result[i])