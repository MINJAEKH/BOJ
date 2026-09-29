def is_valid(answer) :
    for x, y, a in answer : 
        if a == 0 : # 기둥
            if (y == 0 or # 바닥 위
                [x, y-1, 0] in answer or # 다른 기둥 위
                [x-1, y, 1] in answer or # 보의 한쪽 끝 부분 위
                [x, y, 1] in answer) : 
                continue
            return False 
        elif a == 1 : # 보
            if (
                [x, y-1, 0] in answer or # 한쪽 끝 부분이 기둥 위
                [x+1, y-1, 0] in answer or 
                (
                    [x-1, y, 1] in answer and # 양쪽 끝 부분이 다른 보와 동시에 연결
                    [x+1, y, 1] in answer
                )
               ): 
                continue
            return False 
    return True

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame : 
        if b == 0 : # 삭제
            answer.remove([x,y,a]) # 일단 삭제하고 조건에 위배되는지 확인
            if not is_valid(answer) : 
                answer.append([x,y,a])
        elif b == 1 : # 설치
            answer.append([x,y,a]) # 일단 설치하고 조건에 위배되는지 확인
            if not is_valid(answer) : 
                answer.remove([x,y,a])
            
    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))