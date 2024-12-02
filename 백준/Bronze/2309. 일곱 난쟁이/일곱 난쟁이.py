import itertools

def find_dwarf(heights) :
    remainder = sum(heights) - 100
    fake_combinations = list(itertools.combinations(heights, 2)) #nC2

    for comb in fake_combinations :
        if sum(comb) == remainder :
            heights.remove(comb[0])
            heights.remove(comb[1])
            break
    return '\n'.join(map(str,sorted(heights))) # inb형 리스트 join

heights = [int(input()) for  _ in range(9)]
print(find_dwarf(heights))