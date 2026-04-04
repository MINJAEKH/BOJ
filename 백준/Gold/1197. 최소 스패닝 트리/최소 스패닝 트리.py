import sys
input = sys.stdin.readline

edges = []
v, e = map(int, input().split())

for _ in range(e) :
    n1, n2, cost = map(int, input().split())
    edges.append([n1, n2, cost])

def kruskal(edges, v) :
    parent = [i for i in range(v+1)]
    r = [0] * (v+1)
    total_cost = 0
    cnt = 0

    edges.sort(key=lambda x : x[2]) # 가중치 오름차순 정렬

    def find(node) :
        nonlocal parent

        if parent[node] != node :
            parent[node] = find(parent[node])
        return parent[node]
    
    def union(root_x, root_y) :
        nonlocal parent, r
        if r[root_x] > r[root_y]:
            parent[root_y] = root_x
        elif r[root_x] < r[root_y]:
            parent[root_x] = root_y
        else: # 높이가 같을 때만
            parent[root_y] = root_x
            r[root_x] += 1 # 한쪽 층수를 높임

    for x, y, cost in edges :
        root_x = find(x)
        root_y = find(y)

        if root_x != root_y :
            union(root_x, root_y)
            total_cost += cost
            cnt += 1

        if cnt == v-1 : 
            break

    return total_cost

answer = kruskal(edges, v)
print(answer)