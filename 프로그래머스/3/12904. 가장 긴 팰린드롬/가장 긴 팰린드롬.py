def is_palindrome(word) :
    left = 0
    right = len(word)-1
    
    while left < right :
        if word[left] != word[right] :
            return False
        else :
            left += 1
            right -= 1
    return True
    
def solution(s):
    answer = 0
    
    for length in range(len(s), 0, -1) : # 7,6,5,4,3,2,1
        if answer > length :
            break
        for i in range(len(s)-length+1) : 
            word = s[i:i+length]
            if is_palindrome(word) :
                #print(f'length = {length}, word = {word}')
                answer = len(word)
    return answer