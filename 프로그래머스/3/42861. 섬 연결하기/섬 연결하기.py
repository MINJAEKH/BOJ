def find(parent,node) : 
    # node가 속한 최상위 부모 찾기
    if parent[node] != node :
        parent[node] = find(parent, parent[node])
    return parent[node]

# 트리가 한쪽으로 너무 길어지는 걸 막기 위함
def union(parent, rank, x, y) :
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def solution(n, costs):
    answer = 0
    edges_cnt = 0
    rank = [0] * n # 트리 높이 
    parent = [i for i in range(n)]  # 자기 자신이 parent node
    
    costs.sort(key = lambda x: x[2]) 
    
    for a, b, cost in costs :
        root_a = find(parent, a)
        root_b = find(parent, b)
        
        # 부모가 다르면 (=서로 다른 무리)
        if root_a != root_b :
            union(parent, rank, root_a, root_b)
            answer += cost
            edges_cnt += 1
            
        # 간선의 개수가 n-1개가 되면 모든 섬 연결 완료
        if edges_cnt == n - 1:
            break
            
        
    return answer