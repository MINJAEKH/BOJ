def solution(prices):
    stack = []
    length = len(prices)
    periods = [ i for i in range (length - 1, -1, -1)]
    
    for i in range(length) :
        while stack and prices[stack[-1]] > prices[i] :
            j = stack.pop()
            periods[j] = i - j
        stack.append(i)
    
    return periods