n, m = map(int,input().split())

scores = list(map(int, input().strip().split()))

scores.sort(reverse = True) 
print(scores[m-1])