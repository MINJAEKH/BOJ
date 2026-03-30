def solution(word):
    answer = 0
    vowels = 'AEIOU'
    found = False
    
    def dfs(new_word) :
        nonlocal found, answer
        
        if word == new_word :
            found = True
            return
        
        if len(new_word) == 5 :
            return
        
        for i in range(5) :
            if not found : 
                answer += 1
                dfs(new_word + vowels[i])
    
    dfs('')
    return answer