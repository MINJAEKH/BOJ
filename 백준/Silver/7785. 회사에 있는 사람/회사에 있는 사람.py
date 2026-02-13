from collections import defaultdict 
n = int(input())

worker_dict = defaultdict(str)

for _ in range(n) :
    name, status = input().strip().split()
    worker_dict[name] = status

result = [k for k,v in worker_dict.items() if v == 'enter']
print(*sorted(result, reverse = True), sep='\n')