from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for start, end in tickets:
        graph[start].append(end)

    # 역순 정렬
    for airport in graph:
        graph[airport].sort(reverse=True)

    result = []

    def dfs(current):
        while graph[current]:
            next_airport = graph[current].pop()
            dfs(next_airport)

        result.append(current)

    dfs("ICN")

    return result[::-1]