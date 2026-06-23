def solution(s):
    stack = []
    
    for bracket in s :
        if bracket == '(' :
            stack.append('(')
        elif bracket == ')' :
            if not stack :  # 스택이 비어있는 경우
                return False
            stack.pop()
    
    if stack :
        return False
    else :
        return True