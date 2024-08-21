n, m = map(int, input().split())
numbers =  list(map(int, input().split()))
numbers.sort()

res = []
def sequence(depth) :
    if depth == m :
        print(' '.join(map(str,res)))
        return
    
    for i in range(n) :
        if numbers[i] in res :
            continue
        #not in res
        res.append(numbers[i])
        sequence(depth+1)
        res.pop() 
        
sequence(0)