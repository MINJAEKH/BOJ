import math

def solution(progresses, speeds):
    answer = []
    
    # 각 작업이 완료되기까지 남은 일수 계산
    days_to_complete = [
        math.ceil((100 - progress)/speed)
        for progress, speed in zip(progresses, speeds)
    ]
    
    cnt = 0
    max_days = days_to_complete[0]
    for day in days_to_complete :
        # 기준일보다 먼저 끝나거나 같이 끝나면 같은 날 배포
        if max_days >= day :
            cnt += 1
        else :
            answer.append(cnt)
            cnt = 1
            max_days = day
    
    # 마지막 배포 그룹 추가 
    answer.append(cnt)
    
    return answer