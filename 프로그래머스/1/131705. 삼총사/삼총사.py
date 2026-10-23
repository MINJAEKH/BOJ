def backtracking(number, depth, start, total) :
    if depth == 3 :
        return 1 if total == 0 else 0
    
    answer = 0
    for i in range(start, len(number)) :
        answer += backtracking(number, depth+1, i+1, total+number[i])
    return answer
    
def solution(number):
    return backtracking(number, 0, 0, 0)
