def solution(answers):
    result = []
    scores = [0]*3
    
    first = [1, 2, 3, 4, 5] # 5
    second = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    for i in range(len(answers)) :
        if answers[i] == first[i%5] :
            scores[0] += 1
        if answers[i] == second[i%8] :
            scores[1] += 1
        if answers[i] == third[i%10] :
            scores[2] += 1
    
    max_score = max(scores)
    for idx, score in enumerate(scores) :
        if score == max_score :
            result.append(idx+1)
    return result