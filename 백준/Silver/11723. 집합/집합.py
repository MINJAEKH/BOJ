import sys
input = sys.stdin.readline

S = set()

for _ in range(int(input())) :
    ls = input().split()
    
    if len(ls) == 1 :
        if ls[0] == 'all' :
            S = set(range(1, 21))
        else : # empty 
            S = set()
            
    else :
        func, num = ls[0], int(ls[1])
        
        if func == 'add' :
            S.add(num)
        elif func == 'remove' :
            S.discard(num) # 틀린 부분
        elif func == 'check' :
            if num in S :
                print(1)
            else :
                print(0)
        elif func == 'toggle' :
            if num in S :
                S.remove(num)
            else :
                S.add(num)
