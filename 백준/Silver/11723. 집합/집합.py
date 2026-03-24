import sys
input = sys.stdin.readline
s = set()

for _ in range(int(input())) :
    ops = input().split()

    if len(ops) == 1:
        op = ops[0]
    else:
        op, x_set = ops[0], {int(ops[1])}

    if op == 'all':
        s = set(range(1, 21))
    elif op == 'empty' :
        s.clear()
    elif op == 'add' :
        s = s | x_set
    elif op == 'remove' :
        s = s - x_set
    elif op == 'check' :
        print(1 if s & x_set else 0)
    elif op == 'toggle' :
        s = s ^ x_set