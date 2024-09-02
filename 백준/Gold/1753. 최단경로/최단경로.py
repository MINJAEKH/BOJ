import sys
input = sys.stdin.readline

import heapq

V, E = map(int, input().split())
K = int(input())

adj = [[] for _ in range(V + 1)]        # 인접 리스트

for _ in range(E):
    s, e, w = map(int, input().split()) # 단방향 그래프
    adj[s].append((w, e))

dist = [987654321] * (V + 1)            # 최단거리 기록할 리스트
heap = []

dist[K] = 0                             # 시작점 설정
heapq.heappush(heap, (0, K))

while heap:                             # 힙이 빌 때까지
    wei, now = heapq.heappop(heap)      # 누적 가중치와 노드 번호를 뽑아서

    if dist[now] < wei:                 # 현재 최적값이 아니라면 패스
        continue

    for w, next_node in adj[now]:       # 다음 갈 수 있는 곳을 탐색해서
        next_wei = wei + w              # 현재 가중치에 다음 가중치를 더한 값이

        if next_wei < dist[next_node]:  # 현재 그 노드로 갈 수 있는 가중치보다 작다면(갱신 가능하다면)
            dist[next_node] = next_wei  # 갱신하고 힙에 넣기
            heapq.heappush(heap, (next_wei, next_node))

for d in dist[1:]:
    if d == 987654321:
        print('INF')
    else:
        print(d)