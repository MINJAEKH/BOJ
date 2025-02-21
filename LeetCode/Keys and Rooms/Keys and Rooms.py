from collections import deque 

class Solution(object):
    def canVisitAllRooms(self, rooms):
        n = len(rooms)
        graph = {}
        visited = [[False]*n]*n
        visited[0][0] = True

        for idx in range(len(rooms)) :
            graph[idx] = rooms[idx]

        queue = deque()
        queue.append(0)
        
        while queue :
            q = queue.popleft()
            #print("q :", q)
            for v in graph[q] :
                print("v :", v)
                if visited[v][v] == False and v != q:
                     visited[v][v] = True
                     #print(v, visited[v][v])
                     queue.append(v)
        
        left_diag = [visited[row][row] for row in range(n)]
        #print(left_diag)
        if left_diag.count(True) == n :
            return True
        return False
