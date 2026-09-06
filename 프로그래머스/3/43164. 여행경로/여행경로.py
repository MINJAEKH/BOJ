from collections import defaultdict

def solution(tickets):
    visited = defaultdict(list)
    routes = defaultdict(list)
    depth = len(tickets) + 1

    for start, end in tickets :
        routes[start].append(end)
        visited[start].append(False)
    for key in routes :
        routes[key].sort()
    
    def dfs(curr, path) :
        if len(path) == depth :
            return path
        
        for idx, nxt in enumerate(routes[curr]):
            if not visited[curr][idx] : 
                visited[curr][idx] = True
                result = dfs(nxt, path + [nxt])
                if result :
                    return result
                visited[curr][idx] = False
                
    return dfs("ICN", ["ICN"])