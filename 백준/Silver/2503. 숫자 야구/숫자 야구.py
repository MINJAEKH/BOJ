import sys
sys.setrecursionlimit(9999999)

def check(idx, number) :
    # input으로 주어진 값
    _number = games[idx][0]
    _strike = games[idx][1]
    _ball = games[idx][2]
    
    _A = _number // 100
    _B = (_number - _A*100) // 10
    _C = _number % 10
    
    # 비교할 값 
    strike = 0
    ball = 0 
    A = number // 100
    B = (number - A*100) // 10
    C = number % 10
    
    if A == 0 or B == 0 or C == 0: # 놓친부분 3
        return False 
    
    if A == B or A == C or B == C: # 놓친부분 2
        return False 
    
    # strke 
    if _A == A :
        strike += 1
    if _B == B :
        strike += 1
    if _C == C :
        strike += 1
    
    # ball 
    if _A == B or _A == C :
        ball += 1
    if _B == A or _B == C :
        ball += 1
    if _C == A or _C == B :
        ball += 1
    
    if _strike == strike and _ball == ball :
        return True
    else : 
        return False 

def baseball(idx, number) :
    global ans 
    
    if number == 988 :
        return
    
    if idx == N : # 4가지 input과 조건이 모두 동일하면
        ans += 1  
        baseball(0, number + 1) 
        return # 놓친부분

    # 현재 숫자가 조건을 만족하는지 체크
    flag = check(idx, number)
    
    if flag : # 다음 input과 비교 
        baseball(idx+1, number)
    else : # 조건 만족하지 않으면 다음 숫자로 이동 
        baseball(0, number + 1)

N = int(input())
games = [list(map(int, input().split())) for _ in range(N)]
ans = 0
baseball(0,123)
print(ans)