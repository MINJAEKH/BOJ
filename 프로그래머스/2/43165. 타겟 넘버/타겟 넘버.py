from collections import deque

def solution(numbers, target):
    n = len(numbers) 
    
    def dfs(idx, total) :
        if idx == n : 
            return 1 if total == target else 0
        
        return dfs(idx+1, total + numbers[idx]) + dfs(idx+1, total - numbers[idx])
        
    return dfs(0,0)
