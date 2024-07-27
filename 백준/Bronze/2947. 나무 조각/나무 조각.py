seq = list(map(int, input().split()))

while seq != [1,2,3,4,5] :
    for i in range(1,5) :
        if seq[i] < seq[i-1] :
            seq[i], seq[i-1] = seq[i-1], seq[i]
            print(*seq) # * : unpacking 연산자 