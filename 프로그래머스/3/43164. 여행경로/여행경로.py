from collections import defaultdict

def dfs(start, visited, graph) :
    while graph[start] :
        next_airport = graph[start].pop()
        #print(f'start = {start}, next = {next_airport}, visited = {visited}')
        dfs(next_airport, visited, graph)
    visited.append(start)
        
def solution(tickets):
    graph = defaultdict(list)
    visited = []
    
    for start, end in tickets :
        graph[start].append(end)
    for key in graph:
        graph[key].sort(reverse = True)
    
    dfs('ICN', visited, graph)
    return visited[::-1]