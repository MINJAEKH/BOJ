def solution(word):
    answer = 0
    flag = False
    vowels = 'AEIOU'
    
    def dfs(curr_word, depth) :
        nonlocal answer, flag
        
        if curr_word == word :
            flag = True
            return
        if depth == 5 :
            return
        
        for v in vowels :
            if flag : 
                break
            answer += 1
            dfs(curr_word + v, depth+1)
            
    dfs('', 0)   
    return answer