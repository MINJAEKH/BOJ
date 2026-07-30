def solution(answers):
    scores = [0]*3
    first = [1, 2, 3, 4, 5] # 5
    second = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    for idx in range(len(answers)) :
        if answers[idx] == first[idx%5] :
            scores[0] += 1
        if answers[idx] == second[idx%8] :
            scores[1] += 1
        if answers[idx] == third[idx%10] :
            scores[2] += 1
    
    m = max(scores)
    return [i + 1 for i in range(len(scores)) if scores[i] == m]