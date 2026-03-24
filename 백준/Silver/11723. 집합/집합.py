import sys
input = sys.stdin.readline
s = set()

for _ in range(int(input())) :
    ops = input().split()

    if len(ops) == 1:
        op = ops[0]
    else:
        op, x = ops[0], int(ops[1])

    if op == 'all':
        s = set(range(1, 21))
    elif op == 'empty' :
        s.clear()
    elif op == 'add' :
        s.add(x)
    elif op == 'remove' :
        s.discard(x)
    elif op == 'check' :
        print(1 if x in s else 0)
    elif op == 'toggle' :
        if x in s :
            s.remove(x)
        else :
            s.add(x)