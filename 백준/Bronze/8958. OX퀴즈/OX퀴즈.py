T = int(input())

for _ in range(T) :
    result = input()
    score = 0
    cnt = 0
    
    for i in range(len(result)) :
        if result[i] == 'X' :
            cnt = 0
        elif result[i] == 'O' :
            cnt += 1
            score += cnt 
    print(score)