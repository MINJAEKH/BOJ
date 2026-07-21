def solution(n, lost, reserve):
    # 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우 고려
    lost_set = set(lost) - set(reserve)
    reserve_set = sorted(set(reserve) - set(lost))

    for i in reserve_set :
        if i-1 in lost_set :
            lost_set.remove(i-1)
        elif i+1 in lost_set :
            lost_set.remove(i+1)
    
    return n - len(lost_set)