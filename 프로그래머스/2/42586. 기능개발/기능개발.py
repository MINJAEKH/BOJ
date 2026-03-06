# 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수도 있고 
# 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함계 배포됨
# progresses :  배포되어야 하는 순서(작업의 진도가 100%로야 함)
# speeds : 개발 속도
# 각 배포마다 몇 개의 기능이 배포되는가?
import math

def solution(progresses, speeds):
    deploys = 0
    completed = []
    answer = []
    
    for progress, speed in zip(progresses, speeds) :
        day = math.ceil((100 - progress) / speed)
        completed.append(day)
    
    ind = 0
    for i in range(len(completed)) :
        if completed[ind] < completed[i] :
            answer.append(i-ind)
            ind = i
    answer.append(i-ind+1)
    return answer