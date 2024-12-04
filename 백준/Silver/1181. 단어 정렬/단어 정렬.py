import sys
input = sys.stdin.readline

N = int(input())

vocab = [input().strip() for _ in range(N)]
vocab = list(set(vocab)) 

tmp = sorted(vocab, key = lambda x : (len(x), x))
for voca in tmp :
    print(voca)