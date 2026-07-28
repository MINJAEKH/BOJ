def solution(routes):
    answer = 0
    camera_loc = -30001
    routes.sort(key=lambda x : x[1])
    
    for start, end in routes :
        if start > camera_loc :
            camera_loc = end
            answer += 1
    return answer