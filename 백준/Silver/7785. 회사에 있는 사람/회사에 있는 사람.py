N = int(input())
record = {}
working = []

for _ in range(N) :
    name, status = input().split()
    record[name] = status

for k, v in record.items() :
    if v == 'enter' :
        working.append(k)
working.sort(reverse= True)
print('\n'.join(working))