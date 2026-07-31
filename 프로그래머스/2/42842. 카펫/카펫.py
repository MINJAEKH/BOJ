def solution(brown, yellow): 
    area = brown + yellow
    
    # 세로 길이는 최소 3 이상이어야 노란색이 들어갈 수 있음
    for h in range(3, int(area**0.5)+1) :
        # w >= h이므로 1~제곱근 사이 값은 h로 설정 가능
        if area % h == 0 : 
            w = area // h
            
            if (w-2) * (h-2) == yellow : 
                return [w,h]