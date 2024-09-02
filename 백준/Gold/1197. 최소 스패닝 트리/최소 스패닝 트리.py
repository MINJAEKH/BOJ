import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
    
edges.sort(key =lambda x : x[2]) # c

# Union-Find
parent = dict()
for i in range(1, v+1):    
    parent[i] = i

def get_parent(x) :
    if parent[x] == x : # node num = parent node num
        return x
    parent[x] = get_parent(parent[x]) 
    return parent[x]

def union_parent(a,b) :
    a = get_parent(a)
    b = get_parent(b)
    
    if a < b : # 작은 쪽이 부모가 된다
        parent[b] = a
    else :
        parent[a] = b
        
def find_same_parent(a,b) : # 같은 그래프 내에 있는지 확인
    return get_parent(a) == get_parent(b)

ans = 0
for a, b, cost in edges :
    if not find_same_parent(a, b) :
        union_parent(a, b) 
        ans += cost
print(ans)