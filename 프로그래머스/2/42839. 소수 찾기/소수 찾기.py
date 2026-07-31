from itertools import permutations

def is_prime(x) :
    if x < 2 :
        return False
    for divisor in range(2, int(x**0.5)+1) :
        if x % divisor == 0 :
            return False
    return True

def solution(numbers):
    answer = 0
    decimal_set = set()
    num_list = list(numbers)
    
    for i in range(1, len(numbers)+1) :
        for p in permutations(num_list, i) :
            num = int(''.join(p))
            if num not in decimal_set and is_prime(num) :
                answer +=1 
                decimal_set.add(num)
    return answer