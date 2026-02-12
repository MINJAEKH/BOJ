from collections import defaultdict

def solution(participant, completion):
    participant_dict = defaultdict(int)

    for name in participant :
        participant_dict[name] += 1
    for name in completion :
        participant_dict[name] -= 1
    
    uncompleted = [k for k,v in participant_dict.items() if v == 1][0]
    return uncompleted
