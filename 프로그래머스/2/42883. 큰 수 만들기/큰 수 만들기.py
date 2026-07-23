def solution(number, k):
    stack = []
    
    for num in number :
        # 스택에 값이 있고/현재 숫자 num이 앞 숫자보다 크고/제거할 기회(k)가 남았다면
        while stack and k > 0 and stack[-1] < num :
            stack.pop()
            k -= 1
        stack.append(num)

    # 아직 제거할 기회가 남은 경우 
    if k > 0 :
        stack = stack[:-k]
        
    return ''.join(stack)