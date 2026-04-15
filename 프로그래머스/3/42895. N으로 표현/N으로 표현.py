def solution(N, number):
    if N == number:
        return 1
    
    S = [set() for _ in range(9)]
    
    for i in range(1, 9):
        S[i].add(int(str(N) * i))
        
        for j in range(1,i) :
            for obj1 in S[j] :
                for obj2 in S[i-j] :
                    S[i].add(obj1 + obj2)
                    S[i].add(obj1 - obj2)
                    S[i].add(obj1 * obj2)
                    
                    if obj2 != 0 :
                        S[i].add(obj1 / obj2)
        if number in S[i] :
            return i
    return -1