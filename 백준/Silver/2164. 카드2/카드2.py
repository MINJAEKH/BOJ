from collections import deque

card_list = [i for i in range(1, int(input())+1)]
card_q = deque()
card_q.extend(card_list)

while len(card_q) != 1 :
    card_q.popleft()
    back = card_q.popleft()
    card_q.append(back)

print(card_q[0])