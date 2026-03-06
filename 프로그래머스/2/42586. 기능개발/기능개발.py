import math

def solution(progresses, speeds):
    completion_days = [
        math.ceil((100 - progress) / speed)
        for progress, speed in zip(progresses, speeds)
    ]
    
    answer = []
    cnt = 0
    current_release_days = completion_days[0]
    for day in completion_days :
        if current_release_days >= day :
            cnt += 1
        else :
            answer.append(cnt)
            current_release_days = day
            cnt = 1
    answer.append(cnt)
    
    return answer