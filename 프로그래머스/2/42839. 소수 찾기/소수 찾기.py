from itertools import permutations

def is_decimal(x) :
    if x < 2 :
        return False
    
    for i in range(2, int(pow(x, 0.5))+1) :
        if x % i == 0 :
            return False
    return True

def solution(numbers):
    answer = 0
    checked = set()
    num_list = list(numbers)
    
    for i in range(1, len(numbers)+1) :
        for p in permutations(numbers, i): 
            num = int(''.join(p))
            if num not in checked and is_decimal(num):
                answer += 1
                #print(f'num = {num}, chekced = {checked}, answer = {answer}')
            checked.add(num)
    return answer