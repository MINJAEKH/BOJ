def solution(brown, yellow):
    area = brown + yellow # 면적
    
    for div in range(3, int(pow(area,0.5))+1) :
        if area % div == 0 :
            w, h = max(area//div, div), min(area//div, div)
            if (w-2)*(h-2) == yellow :
                return [w,h]